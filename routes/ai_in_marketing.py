from flask import Blueprint, render_template

ai_in_marketing = Blueprint('ai_in_marketing', __name__)

@ai_in_marketing.route('/ai-in-marketing')
def show_ai_in_marketing():
    return render_template("ai_in_marketing.html", title="AI In Marketing")
