from flask import Blueprint, render_template, session

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
def show_dashboard():
    # Session-based hit tracker (or static mock for now)
    session['hits'] = session.get('hits', 0) + 1

    # ✅ Sample hits dictionary
    hits_dict = {
        "pandas": 3,
        "markdown engine": 2,
        "sap + ai": 1
    }

    # ✅ Sample article metadata
    articles_count = 18
    last_updated = "16 July, 2025"

    return render_template(
        "dashboard.html",
        title="Lab Dashboard",
        hits=hits_dict,
        articles_count=articles_count,
        last_updated=last_updated
    )

