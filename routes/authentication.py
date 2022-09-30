from flask import request, session
from routes import db
from application.controller.authentication.login import login_get, login_post
from application.controller.authentication.logout import logout_get
from application.controller.authentication.register import register_get, register_post
from flask import Blueprint

authentication = Blueprint("authentication", __name__)

@authentication.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == "POST":
        return login_post(request, session)

    if request.method == "GET":
        return login_get()

@authentication.route('/logout', methods = ['GET', 'POST'])
def logout():
    if request.method == "GET":
        return logout_get(session)

@authentication.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == "POST":
        return register_post(request, db)

    if request.method == "GET":
        return register_get()