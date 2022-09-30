from flask import redirect, url_for
from flask_login import current_user
def logout_enterprise_get(session):
    if current_user.is_authenticated and session['type'] == 2:
        session['type'] = 1
        session.pop("id_enterprise", None)
        
    return redirect(url_for("index"))
        