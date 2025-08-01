from flask import Blueprint, render_template, request
import os, markdown

tool_viewer = Blueprint('tool_viewer', __name__)

@tool_viewer.route('/tool-viewer/<name>')
def view_tool_story(name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    story_path = os.path.join(base_dir, '..', 'docs', 'tools_stories', f'{name}.md')

    if not os.path.exists(story_path):
        return "❌ Story not found", 404

    with open(story_path, 'r', encoding='utf-8') as f:
        content = markdown.markdown(f.read())

    return render_template("tool_viewer.html", content=content, title=name.title())
