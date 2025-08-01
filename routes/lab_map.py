from flask import Blueprint, render_template

lab_map = Blueprint('lab_map', __name__)

@lab_map.route('/lab_map')
def show_lab_map():
    return render_template("lab_map.html", title="Lab Map")