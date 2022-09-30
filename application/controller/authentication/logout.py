from flask_login import logout_user

from flask import redirect, url_for
def logout_get(session):

    logout_user()

    if session['type'] == 2:
        session.pop("id_enterprise", None)

    session.pop("type", None)
        
    return redirect(url_for("index"))