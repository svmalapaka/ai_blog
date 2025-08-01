from flask import Blueprint, render_template

ai_in_ethics = Blueprint('ai_in_ethics', __name__)

@ai_in_ethics.route('/ai-in-ethics')
def show_ai_in_ethics():
    return render_template("ai_in_ethics.html", title="AI In Ethics")
