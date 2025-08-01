from flask import Flask, render_template, jsonify, send_from_directory, abort, request
import os
import requests
import markdown
import frontmatter
import glob
import  openai
from services.ai_engine import respond_to_user
import re  # ← This is the missing piece
from datetime import datetime
from slugify import slugify
from scripts.logger import log_entry
from dotenv import load_dotenv
from openai import OpenAI
import markdown2
from diagnostics.openai_check import validate_openai_key
from diagnostics.copilot_check import check_copilot_status
from diagnostics.tunnel_check import test_tunnel_connection
from diagnostics.markdown_check import check_markdown_renderer
from utils.session_check import verify_session_tracking
from services.markdown_index import generate_md_index
from helpers import generate_md_index
# ⬇️ Add your function here
def load_lab_log():
    with open("tools/lab-log.md", "r", encoding="utf-8") as f:
        raw_md = f.read()
    return markdown.markdown(raw_md)

load_dotenv(dotenv_path="config/.env")  # Or default to just load_dotenv() if .env is in the root
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__, template_folder="templates")  # Single app declaration
app.jinja_env.filters["slugify"] = slugify

# 📁 Path setup
TOOLS_PATH = os.path.join(os.getcwd(), 'docs', 'tools_stories')

# 🔍 Health check function
def check_lab_map():
    try:
        response = requests.get("http://localhost:5001/lab-map")
        return response.status_code == 200
    except:
        return False

# 🧠 Extract front matter from Markdown
def extract_front_matter(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.match(r"---\n(.*?)\n---", content, re.DOTALL)
    front = match.group(1) if match else ""
    data = {}
    for line in front.split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data

# 📘 Load markdown files as tool stories
def load_tool_stories():
    stories = []
    for filename in os.listdir(TOOLS_PATH):
        if filename.endswith(".md"):
            full_path = os.path.join(TOOLS_PATH, filename)
            title = filename.replace("_", " ").replace(".md", "").title()
            slug = filename.replace(".md", "")
            meta = extract_front_matter(full_path)
            stories.append({
                "name": meta.get("title", title),
                "url": f"/tools/{slug}",
                "summary": meta.get("summary", ""),
                "tags": [tag.strip() for tag in meta.get("tags", "").split(",")] if "tags" in meta else []
            })
    stories.sort(key=lambda x: x["name"])
    return stories

# 🌐 ROUTES

@app.route('/unit-7')
def unit_7():
    with open('templates/markdown/unit-7-trigonometry-analysis.md', 'r', encoding='utf-8') as f:
        md_content = f.read()

    rendered_markdown = markdown2.markdown(md_content, extras=["fenced-code-blocks", "tables"])
    return render_template('unit_7.html', rendered_markdown=rendered_markdown)

@app.route("/tools/debug/slugs")
def debug_slugs():
    from pathlib import Path
    files = Path("docs/tools_stories").glob("*.md")
    slugs = [f.stem for f in files]
    return "<br>".join(slugs)

@app.route("/tools/validate-links")
def validate_links():
    broken = []
    for entry in generate_md_index():
        path = os.path.join(TOOLS_PATH, f"{entry['slug']}.md")
        if not os.path.exists(path):
            broken.append(entry['slug'])
    return jsonify({"broken_links": broken})


@app.route("/chat")
def chat():
    return render_template("chat.html", show_widget=True)
@app.route('/api/respond', methods=['POST'])
def respond():
    if not request.is_json:
        return jsonify({'reply': 'Invalid request format. Expected JSON.'}), 400

    user_message = request.json.get('message', '').strip().lower()

    replies = {
        "what does jinja2 do": "Jinja2 is a templating engine for Python — it lets you embed dynamic content in HTML using logic like loops and conditionals.",
        "how does scikit-learn work": "scikit-learn is a machine learning library for Python — it simplifies training models, evaluating them, and performing predictions using simple APIs.",
        "what is html for": "HTML structures the content of web pages — it defines elements like headings, links, paragraphs, and forms."
    }

    if user_message in replies:
        response_text = replies[user_message]
        print("🧾 Static reply used:", response_text)
    else:
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": user_message}]
            )
            response_text = response.choices[0].message.content
            print("🤖 AI reply used:", response_text)
        except Exception as err:
            print("⚠️ AI call failed:", err)
            response_text = "Sorry, I couldn’t generate a response right now. Try again soon?"

    return jsonify({'reply': response_text}), 200
@app.route('/diagnostics')
def diagnostics():
    results = {
        "copilot_status": check_copilot_status(),
        "openai_auth": validate_openai_key(),
        "cloudflare_tunnel": test_tunnel_connection(),
        "markdown_parsing": check_markdown_renderer(),
        "session_state": verify_session_tracking()
    }
    return jsonify(results)

@app.route('/debug')
def debug():
    return jsonify({
        "api_key_loaded": bool(openai.api_key),
        "env_loaded": os.getenv("OPENAI_API_KEY") is not None
    })

@app.route('/log-widget', methods=['POST'])
def log_widget():
    user_id = request.json.get('user_id', 'anonymous')
    timestamp = datetime.now().isoformat()
    print(f"Widget launched by {user_id} at {timestamp}")
    return jsonify({'status': 'logged'})

@app.route("/python-portal")
def portal():
    config = {}  # Replace with load_portal_config() if defined elsewhere
    return render_template("portal.html", config=config)

@app.route("/tools/tag/<tag>")
def tag_view(tag):
    markdown_files = glob.glob("your_markdown_folder_path/*.md")  # ✅ Update the actual path
    posts = []
    for path in markdown_files:
        post = frontmatter.load(path)
        if tag in post.get("tags", []):
            posts.append(post)
    return render_template("tag_page.html", posts=posts, tag=tag)

#@app.route("/tools", strict_slashes=False)

#def tools_home():
#    log_entry("Accessed tools dashboard", tags=["flask", "tools", "lab"])
#    return render_template("tool_template.html", ...)

@app.route("/lab-log")
def lab_log():
    logs_raw = sorted([
        f for f in os.listdir(TOOLS_PATH)
        if f.endswith('.md') and 'log' in f
    ])

    logs = [
        {
            "slug": f.replace('.md', ''),
            "title": f.replace('.md', '').replace('-', ' ')
        }
        for f in logs_raw
    ]

    return render_template("lab_log.html", logs=logs)

@app.route("/tools/diagnostics")
def tools_diagnostics():
    try:
        files = os.listdir(TOOLS_PATH)
        return "<br>".join(f for f in files if f.endswith('.md'))
    except Exception as e:
        return f"Error reading TOOLS_PATH: {e}"

@app.route("/tools-stories_index")
def tools_stories_index():
    links = load_tool_stories()
    return render_template("tools_stories_index.html", links=links)

@app.route('/tools/<slug>')
def render_tool_page(slug):
    file_path = os.path.join(TOOLS_PATH, f"{slug}.md")
    abs_file_path = os.path.abspath(file_path)

    print(f"📁 Looking for file at: {abs_file_path}")
    print(f"📂 Current working directory: {os.getcwd()}")
    print(f"📌 TOOLS_PATH resolved as: {os.path.abspath(TOOLS_PATH)}")

    try:
        all_md_files = [
            os.path.abspath(os.path.join(TOOLS_PATH, f))
            for f in os.listdir(TOOLS_PATH)
            if f.endswith('.md')
        ]
        print(f"📄 Markdown files found:\n{all_md_files}")
    except Exception as scan_err:
        print(f"⚠️ Error scanning TOOLS_PATH: {scan_err}")
        print(f"🧵 Checking for: {os.path.join(TOOLS_PATH, f'{slug}.md')}")
        print(f"📂 Current working directory: {os.getcwd()}")
        print(f"📌 TOOLS_PATH resolved to: {os.path.abspath(TOOLS_PATH)}")

        all_md_files = [f for f in os.listdir(TOOLS_PATH) if f.endswith('.md')]
        print(f"📄 Markdown files seen:\n{all_md_files}")
    if not os.path.exists(abs_file_path):
        print(f"❌ File not found — aborting with 404")
        abort(404)

    try:
        post = frontmatter.load(abs_file_path)
        html_body = markdown.markdown(post.content, extensions=["extra", "codehilite", "tables"])
        title = post.get('title', slug.replace('_', ' ').title())
        raw_tags = post.get('tags', [])
        tags = raw_tags if isinstance(raw_tags, list) else [tag.strip() for tag in raw_tags.split(',')]
        author = post.get('author', 'Unknown Author')
        last_updated = post.get('last_updated', 'Unknown Date')
        category = post.get('category', 'General')

        log_entry(f"Viewed post: {slug}", tags=["markdown", "viewer", slug])

        return render_template(
            'tool_template.html',
            title=title,
            author=author,
            last_updated=last_updated,
            category=category,
            tags=tags,
            content=html_body,
            slug=slug
        )

    except Exception as load_err:
        print(f"🧨 Error loading or parsing Markdown file: {load_err}")
        abort(500)



@app.route("/dashboard")
def dashboard():
    status_report = {
        "articles_count": 17,
        "last_updated": datetime.now().strftime("%I:%M %p"),
        "hits": {"flask": 3, "ai": 7, "sap": 2, "markdown": 1}
    }
    return render_template("dashboard.html", **status_report)

@app.route("/tools", strict_slashes=False)
def tools_home():
    log_entry("Accessed tools dashboard", tags=["flask", "tools", "lab"])
    return render_template(
        "tool_template.html",
        title="Lab Tools Dashboard",
        author="Sastry",
        category="Lab Utilities",
        last_updated="2025-07-29",
        tags=["lab", "progress", "log"],
        content="<p>Welcome to your lab tools hub. Choose a tag to explore categorized logs.</p>",
        slug="lab-tools-dashboard"
    )
@app.route("/route-dashboard-text")
def route_dashboard_text():
    last_checked = datetime.now().strftime("%I:%M %p")
    output = f"""
    System Health Overview
    /dashboard: 🟢 Online
    /lab-map: 🔴 Down
    /launch-status: 🟢 Stable
    Last checked: {last_checked}
    """
    return output, 200
@app.route("/tools/post/lab-tools-dashboard")
def lab_tools_dashboard():
    return render_tool_page(slug="lab-tools-dashboard")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/launch-status")
def launch_status():
    return render_template("launch_status.html")

@app.route("/lab-map")
def lab_map():
    return render_template("lab_map.html")

@app.route("/internal/lab-health")
def lab_health():
    status = check_lab_map()
    return f"Lab Map Health: {'🟢 Up' if status else '🔴 Down'} - Last checked: {datetime.now()}", 200

@app.route("/status")
def status():
    return "Flask is healthy and reachable.", 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
@app.route("/tools/index")
def tools_index():
    md_index = generate_md_index()
    return render_template("tools_index.html", entries=md_index)

@app.route("/tools/post/logs_index")
def logs_index():
    log_dir = "docs/tools_stories"
    logs = sorted(os.listdir(log_dir), reverse=True)  # newest first
    slugs = [filename[:-3] for filename in logs if filename.endswith(".md")]
    return render_template("dashboard.html", logs=slugs)



# 🛠️ Optional Debug
def debug_template_listing():
    templates_path = os.path.join(os.path.dirname(__file__), 'templates')
    try:
        template_files = os.listdir(templates_path)
        print("\n🗂️ Templates visible to Flask:")
        for f in template_files:
            status = "✅" if f == "index.html" else "🔹"
            print(f" {status} {f}")
    except FileNotFoundError:
        print("⚠️ templates/ folder not found.")

debug_template_listing()


# Bottom: Single launch block
if __name__ == "__main__":
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint:25} ➤ {rule}")
    app.run(host="127.0.0.1", port=8081, debug=True)

