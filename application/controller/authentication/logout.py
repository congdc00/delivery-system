from flask import redirect, url_for
def logout_get(session):
    session.pop("session_key", None)
    session.pop("admin", None)
    if 'enterprise' in session:
        session.pop("enterprise", None)
        
    return redirect(url_for("index"))