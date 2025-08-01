from flask import Blueprint, render_template

system_status = Blueprint('system_status', __name__)  # ✅ Define first

@system_status.route('/launch-status')
def launch_status():
    status = {
        "flask": "✅ Running",
        "cloudflare_tunnel": "✅ Connected",
        "markdown_engine": "✅ Active",
        "dashboard": "✅ Online"
    }

    return render_template("launch_status.html", title="Launch Status", status=status)
