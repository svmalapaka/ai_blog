from flask import session

def verify_session_tracking():
    try:
        session['test'] = 'active'
        return "✅ Session tracking functional"
    except Exception as e:
        return f"❌ Session error: {str(e)}"