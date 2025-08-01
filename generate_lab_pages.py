import os

# 🔹 Topic definitions
topics = [
    "ai_in_finance",
    "ai_in_hr",
    "ai_in_healthcare",
    "ai_in_marketing",
    "ai_in_supplychain",
    "ai_in_education",
    "ai_in_ethics"
]

# 🔧 File paths
routes_dir = os.path.join("routes")
templates_dir = os.path.join("templates")

# 🛠️ Ensure directories exist
os.makedirs(routes_dir, exist_ok=True)
os.makedirs(templates_dir, exist_ok=True)

# 🧠 File generator
for topic in topics:
    # Format title
    title = topic.replace("_", " ").title().replace("Ai", "AI")

    # 🔹 .py route file
    route_code = f"""from flask import Blueprint, render_template

{topic} = Blueprint('{topic}', __name__)

@{topic}.route('/{topic.replace('_', '-')}')
def show_{topic}():
    return render_template("{topic}.html", title="{title}")
"""
    with open(os.path.join(routes_dir, f"{topic}.py"), "w") as py_file:
        py_file.write(route_code)

    # 🔹 .html template
    html_code = f"""{{% extends "base.html" %}}
{{% block content %}}
<h2>{{{{ title }}}}</h2>
<p>This page will explore how {title} intersects with real tools, success stories, and lessons learned.</p>
{{% endblock %}}
"""
    with open(os.path.join(templates_dir, f"{topic}.html"), "w") as html_file:
        html_file.write(html_code)

print("✅ Route and template files generated successfully.")