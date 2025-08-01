# 🧠 Welcome to My AI/ML Learning Lab
## 🌍 Live Lab Access  
Explore the full AI Blog Lab:  
🔗 [https://lab.mvsastry.dev](https://lab.mvsastry.dev)
![License](https://img.shields.io/github/license/svmalapaka/ai_blog)
![Build](https://img.shields.io/github/actions/workflow/status/svmalapaka/ai_blog/python-app.yml?branch=master)
![Python](https://img.shields.io/badge/Python-3.11-blue)

This lab is a personal playground and open-source showcase of how Python tools power real-world AI/ML workflows.  
It’s organized to blend storytelling, diagnostics, and interactive features — like a mini Copilot that guides visitors across the platform.

---

## 🗂️ Project Structure

```plaintext
ai_blog/
├── app.py                  ← Flask app that serves pages, routes, and widgets
├── docs/                   ← Guides, tutorials, and tool stories
│   ├── copilot_micro_widget.md   ← Tutorial for building an AI helper widget
│   ├── lab_routes.md             ← Diagnostic routes like /launch-status
│   └── tools_stories/            ← Story-driven tutorials for core Python tools
│       ├── flask_for_human_apps.md
│       └── how_tensorflow_builds_brains.md
├── static/                 ← CSS and JS files for styling widgets and tools
│   └── copilot_widget.css       ← Styles for the embedded assistant box
├── templates/              ← Jinja2 HTML templates for rendering pages
│   └── base.html                ← Universal layout with embedded Copilot widget
