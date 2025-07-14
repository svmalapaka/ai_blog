from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

RESPONSE_MAP = {
    "pandas": "📊 Pandas helps you load, clean, and shape data — great for wrangling raw datasets before training ML models.",
    "flask": "⚙️ Flask hosts your app and serves routes like /lab-log and /tools/stories/index — simple, powerful, flexible.",
    "jinja2": "🎨 Jinja2 powers dynamic HTML rendering — it loops over your Markdown entries and injects variables with ease.",
    "tensorflow": "🧠 TensorFlow builds neural networks — great for modeling brain-like behavior with layers, activations, and loss functions.",
    "numpy": "⚙️ NumPy gives you fast matrix operations, array transformations, and the data engine under every ML workflow.",
    "matplotlib": "📈 Matplotlib lets you visualize insights — whether it’s trends, clusters, or loss curves during training.",
    "scikit-learn": "🤖 Scikit-learn helps you run predictions and build models like decision trees, SVMs, or KNN — plug and play ML."
}

@app.route('/copilot-widget-query', methods=['POST'])
def widget_query():
    query = request.json.get('query', '').lower()
    for keyword, reply in RESPONSE_MAP.items():
        if keyword in query:
            return jsonify({'response': reply})
    fallback = (
        "Hmm... I didn’t catch that. You can try asking about:\n"
        "• Pandas\n• Flask\n• TensorFlow\n• Jinja2\n"
        "Or check out the /tools_stories_index page for more!"
    )
    return jsonify({'response': fallback})
import markdown
import os

@app.route('/lab-log')
def lab_log():
    md_path = os.path.join('docs', 'lab_log.md')
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content)
    return render_template('lab_log_viewer.html', content=html_content, title="AI Lab Log")

@app.route('/featured-tool')
def featured_tool():
    featured = {
        "name": "Flask",
        "summary": RESPONSE_MAP.get("flask"),
        "link": "/tool-viewer/flask_for_human_apps"
    }
    return render_template("featured_tool.html", featured=featured, title="Featured Tool")


@app.route('/md-viewer/<name>')
def md_viewer(name):
    md_path = os.path.join('docs', f"{name}.md")
    if not os.path.exists(md_path):
        return render_template("404.html", title="Not Found"), 404
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html = markdown.markdown(content)
    return render_template("md_viewer.html", content=html, title=name.replace('_', ' ').title())

@app.route('/lab-map')
def lab_map():
    return render_template("lab_map.html", title="Lab Map")


@app.route('/backup-status')
def backup_status():
    files_to_check = [
        'app.py',
        os.path.join('docs', 'lab_log.md'),
        os.path.join('docs', 'tools_stories', 'flask_for_human_apps.md')
    ]
    status = {}
    for path in files_to_check:
        status[path] = os.path.exists(path)
    return render_template("backup_status.html", status=status, title="Backup Status")



@app.route('/tool-viewer/<name>')
def tool_viewer(name):
    story_path = os.path.join('docs', 'tools_stories', f"{name}.md")
    if not os.path.exists(story_path):
        return render_template("404.html", title="Not Found"), 404
    with open(story_path, 'r', encoding='utf-8') as f:
        content = f.read()
    html = markdown.markdown(content)
    return render_template("tool_viewer.html", content=html, title=name.replace('_', ' ').title())

@app.route('/launch-status')
def launch_status():
    status = {
        "flask_routes": [rule.rule for rule in app.url_map.iter_rules()],
        "widget_active": True,
        "cloudflare_tunnel": "Check using external script or flag",
        "markdown_log_loaded": os.path.exists(os.path.join('docs', 'lab_log.md'))
    }
    return render_template("launch_status.html", status=status, title="Launch Status")



@app.route('/tools_stories_index')
def tools_stories_index():
    stories_path = os.path.join('docs', 'tools_stories')
    files = [f for f in os.listdir(stories_path) if f.endswith('.md')]
    links = [
        {'name': f[:-3].replace('_', ' ').title(), 'url': f"/tool-viewer/{f[:-3]}"}
        for f in files
    ]
    return render_template('tools_stories_index.html', links=links, title="Tool Stories Index")



@app.route('/')
def index():
    return render_template('index.html', title="AI Lab Home")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)


