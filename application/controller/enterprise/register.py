from flask import render_template, redirect, url_for
from flask_login import current_user
def register_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            return render_template("enterprise/register.html")
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
        

    