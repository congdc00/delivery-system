from flask import render_template, redirect, url_for
def register_e_get(session):

    try:
        session_key = session["session_key"]
        admin = session['admin']
        
    except:
        return redirect(url_for("index"))

    return render_template("enterprise/register_enterprise.html", session_key = session_key, admin = admin)