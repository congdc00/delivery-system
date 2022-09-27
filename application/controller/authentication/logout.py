from flask import redirect, url_for
def logout_get(session):
    session.pop("session_key", None)
    session.pop("admin", None)
    return redirect(url_for("index"))