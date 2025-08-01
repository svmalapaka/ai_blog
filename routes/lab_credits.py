from flask import Blueprint, render_template

lab_credits = Blueprint('lab_credits', __name__)

@lab_credits.route('/lab-credits')
def show_credits():
    return render_template("lab_credits.html", title="Lab Credits")
