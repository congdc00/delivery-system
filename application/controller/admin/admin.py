from flask import render_template

def admin_get():
    return render_template("admin/admin.html", session_key = "admin" ,admin = True)