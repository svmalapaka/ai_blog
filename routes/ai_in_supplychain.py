from flask import Blueprint, render_template

ai_in_supplychain = Blueprint('ai_in_supplychain', __name__)

@ai_in_supplychain.route('/ai-in-supplychain')
def show_ai_in_supplychain():
    return render_template("ai_in_supplychain.html", title="AI In Supplychain")
