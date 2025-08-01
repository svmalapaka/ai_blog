from flask import Blueprint, render_template

ai_in_finance = Blueprint('ai_in_finance', __name__)

@ai_in_finance.route('/ai-in-finance')
def show_ai_in_finance():
    return render_template("ai_in_finance.html", title="AI In Finance")
