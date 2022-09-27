
from flask import request, redirect, url_for, render_template, session,flash
from flask_cors import cross_origin

from application.models import enterprise
from . import app
from app import db
from loguru import logger
from application.controller.authentication.register import register_post, register_get
from application.controller.authentication.login import login_post, login_get
from application.controller.user.info import info_post,info_get
from application.controller.admin.admin import admin_get
from application.controller.authentication.logout import logout_get
from application.controller.admin.setting import setting_get
from application.controller.user.u2e import u2e_get, u2e_post
from application.controller.enterprise.register_enterprise import register_e_get

@app.route('/', methods = ['POST', 'GET'])
@cross_origin(origins='*')
def index():
    if "session_key" in session:
        session_key = session['session_key']
        admin = session['admin']

        if "enterprise" in session:
            enterprise = session['enterprise']
            return render_template("index.html", session_key = session_key, admin = admin, enterprise = enterprise)

        return render_template("index.html", session_key = session_key, admin = admin)
    else:
        return render_template("index.html")

@app.route('/admin', methods = ['GET'])
@cross_origin(origins='*')
def admin():
    if request.method == "GET":
        if 'admin' in session and session['admin']:
            return admin_get()

        return redirect(url_for("index"))

@app.route('/info', methods = ['GET'])
@cross_origin(origins='*')
def info_user():
    if request.method == "POST":
        return info_post(request, session)
    
    if request.method == "GET":
        return info_get(db, session)

@app.route('/login', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def login():
    
    if request.method == "POST":
        return login_post(request, session, db)

    if request.method == "GET":
        return login_get()

@app.route('/logout', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def logout():
    if request.method == "GET":
        return logout_get(session)

@app.route('/register', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def register():
    if request.method == "POST":
        result = register_post(request, db)
        return render_template(result)

    if request.method == "GET":
        return register_get()

@app.route('/setting', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def setting():
    if request.method == "GET":
        return setting_get(session)

@app.route('/user-to-enterprise', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def u2e():
    if request.method == "GET":
        return u2e_get(session)
    
    if request.method == "POST":
        return u2e_post(session, request)

@app.route('/register-enterprise', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def register_enterprise():
    if request.method == "GET":
        return register_e_get(session)

@app.route('/logout-enterprise', methods = ['GET', 'POST'])
@cross_origin(origins='*')
def logout_enterprise():
    if request.method == "GET":
        if "enterprise" in session:
            session.pop("enterprise", None)
            return redirect(url_for('index'))

# @app.route('/add', methods = ['POST', 'GET'])
# @cross_origin(origins='*')
# def add():
#     a = request.form.get("a")
#     b = request.form.get("b")
#     result = int(a) + int(b)
#     return "Ham cong = " + str(result)
    


