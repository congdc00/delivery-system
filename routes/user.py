from flask import request, session
from routes import db
from application.controller.user.info import info_post, info_get
from application.controller.user.manage_enterprise import list_enterprise, login_enterprise
from application.controller.user.revenue import revenue_get, revenue_post
from flask import Blueprint

user = Blueprint("user", __name__)

@user.route('/info', methods = ['GET'])
def info_user():
    if request.method == "POST":
        return info_post()
    
    if request.method == "GET":
        return info_get(session)

@user.route('/manage-enterprise', methods = ['GET', 'POST'])
def manage_enterprise():
    if request.method == "GET":
        return list_enterprise()
    
    if request.method == "POST":
        return login_enterprise(session, request)

@user.route('/revenue', methods = ['GET', 'POST'])
def revenue_user():
    if request.method == "GET":
        return revenue_get(session)
    
    if request.method == "POST":
        return revenue_post(session, request)