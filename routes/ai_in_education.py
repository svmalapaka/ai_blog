from flask import Blueprint, render_template

ai_in_education = Blueprint('ai_in_education', __name__)

@ai_in_education.route('/ai-in-education')
def show_ai_in_education():
    return render_template("ai_in_education.html", title="AI In Education")
