from flask import flash, redirect, url_for, render_template
from application.models.user import User

def login_post(request, session, db):
    email_address = request.form['emailAddress']
    password = request.form['password']
    if email_address and password:

        user = User.query.filter_by(email = email_address).first()
        if user:
            if password == user.password:
                session.permanent = True
                session['session_key'] = email_address
                session['admin'] = user.admin

                flash("Bạn đã đăng nhập thành công!", "info")
                return redirect(url_for("index"))
        
        flash("Email hoặc mật khẩu không đúng", "error")
        return render_template("authentication/login.html") 
    else:
        flash("Hãy điền đủ gmail và mật khẩu khẩu", "warring")
        return render_template("authentication/login.html")

def login_get():
    return render_template("authentication/login.html")