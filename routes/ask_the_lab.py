from flask import Blueprint, render_template, request, session, redirect

ask_the_lab = Blueprint('ask_the_lab', __name__)

# 🧠 Example static Q&A map
RESPONSE_MAP = {
    "pandas": {
        "text": "Pandas is a powerful Python library for data analysis.",
        "link": "/tool-viewer/pandas_basics"
    },
    # Add more queries as needed
}

@ask_the_lab.route('/ask-the-lab')
def ask_the_lab_route():
    query = request.args.get('query', '').lower()
    entry = RESPONSE_MAP.get(query)

    reply_text = entry["text"] if entry else "🤔 I’m still learning about that topic."
    reply_link = entry["link"] if entry and "link" in entry else None

    if "recent_queries" not in session:
        session["recent_queries"] = []

    if query and entry and query not in session["recent_queries"]:
        session["recent_queries"].insert(0, query)
        session["recent_queries"] = session["recent_queries"][:5]

    return render_template(
        "ask_the_lab.html",
        query=query.title(),
        reply=reply_text,
        link=reply_link,
        recent=session["recent_queries"]
    )
