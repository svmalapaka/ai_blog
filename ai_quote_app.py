from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

quotes = [
    "🧠 'The best way to learn AI is to build something with it.'",
    "🚀 'Start simple. Then scale.'",
    "📊 'Data quality beats model complexity.'",
    "🤖 'Every model is wrong, but some are useful.'",
    "🔍 'Debugging is 80% of machine learning.'"
]


DEBUG_TEMPLATE = False

@app.route("/")
def home():
    if DEBUG_TEMPLATE:
        return "🚨 Flask route is responding — template skipped!"
    return render_template("index.html", title="Home")

@app.route("/quote")
def get_quote():
    return jsonify({"quote": random.choice(quotes)})

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/resources")
def resources():
    return render_template("resources.html", title="Resources")

@app.route("/projects")
def projects():
    return render_template("projects.html", title="Projects")

@app.route("/posts/<post>")
def posts(post):
    return render_template(f"posts/{post}", title=post.replace("-", " ").title())

@app.route("/docs")
def docs():
    return render_template("docs.html", title="Docs")

for rule in app.url_map.iter_rules():
    print(rule.endpoint, rule.rule)

print("✅ Reached app.run()")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
