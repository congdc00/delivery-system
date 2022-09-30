from flask import request, session
from routes import db
from application.controller.enterprise.info import info_post, info_get
from application.controller.enterprise.register import register_get
from application.controller.enterprise.logout import logout_enterprise_get
from application.controller.enterprise.revenue import revenue_get, revenue_post

from flask import Blueprint

enterprise = Blueprint("enterprise", __name__)



@enterprise.route('/info', methods = ['GET'])
def info_enterprise():
    if request.method == "POST":
        return info_post()
    
    if request.method == "GET":
        return info_get(session)

@enterprise.route('/register', methods = ['GET', 'POST'])
def register_enterprise():
    if request.method == "GET":
        return register_get(session)

@enterprise.route('/logout', methods = ['GET', 'POST'])
def logout_enterprise():
    if request.method == "GET":
        return logout_enterprise_get(session)

@enterprise.route('/revenue', methods = ['GET', 'POST'])
def revenue_enterprise():
    if request.method == "GET":
        return revenue_get(session)
    
    if request.method == "POST":
        return revenue_post(session, request)

