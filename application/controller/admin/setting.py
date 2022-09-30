from flask import redirect, url_for, render_template
from flask_login import current_user

def setting_get(session):
    if current_user.is_authenticated:
        if session['type'] == 0:
            return render_template("admin/setting.html")
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))