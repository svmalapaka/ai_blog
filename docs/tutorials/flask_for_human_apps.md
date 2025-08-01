# 🧠 Flask for Human Apps

Welcome to a human-readable guide to Flask — whether you're a curious beginner or a pragmatic tinkerer.

## 🔧 What Is Flask?

Flask is a lightweight Python framework that lets you turn ideas into web apps quickly.  
You write a function, decorate it, and boom — it’s live as a webpage.

## 🗂️ How Your Lab Uses Flask

- `Blueprints` to modularize logic  
- `render_template()` to serve HTML + dynamic variables  
- Markdown stories rendered via routes like `/tool-viewer/<name>`

## 🛠️ Code Sample: Tool Viewer Route

```python
@tool_viewer.route('/tool-viewer/<name>')
def view_tool_story(name):
    ...
