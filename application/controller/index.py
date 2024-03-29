from flask import render_template
from flask_login import current_user

def index_get(session):
    if current_user.is_authenticated:

        if session['type'] == 0:
            return render_template("admin/dashboard.html")
        elif session['type'] == 1:
            return render_template("user/dashboard.html")
        else:
            return render_template("enterprise/dashboard.html")
    else:
        return render_template("index.html")