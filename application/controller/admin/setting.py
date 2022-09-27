from flask import render_template
def setting_get(session):
    if "session_key" in session:
        session_key = session['session_key']
        admin = session['admin']
        return render_template("admin/setting.html", session_key = session_key, admin = admin)
    else:
        return render_template("index.html")