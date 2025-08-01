from flask import Blueprint, render_template
import os

lab_log = Blueprint('lab_log', __name__)

@lab_log.route('/lab-log')
def show_lab_log():
    log_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'lab-log-2025-07-14.md')
    if not os.path.exists(log_path):
        return "🚫 Log not found", 404

    with open(log_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return render_template("tool_viewer.html", content=content, title="Lab Log")
