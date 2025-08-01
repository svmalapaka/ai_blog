from flask import Blueprint, render_template

ai_in_healthcare = Blueprint('ai_in_healthcare', __name__)

@ai_in_healthcare.route('/ai-in-healthcare')
def show_ai_in_healthcare():
    return render_template("ai_in_healthcare.html", title="AI In Healthcare")
