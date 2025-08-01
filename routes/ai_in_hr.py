from flask import Blueprint, render_template

ai_in_hr = Blueprint('ai_in_hr', __name__)

@ai_in_hr.route('/ai-in-hr')
def show_ai_in_hr():
    return render_template("ai_in_hr.html", title="AI In Hr")
