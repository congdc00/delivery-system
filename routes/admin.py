from flask import request, session
from routes import db
from application.controller.admin.setting import setting_get
from application.controller.admin.notification import notification_get, notification_post
from application.controller.admin.scheduler_map import scheduler_map_get, scheduler_map_post
from flask import Blueprint

admin = Blueprint("admin", __name__)

@admin.route('/setting', methods = ['GET', 'POST'])
def setting():
    if request.method == "GET":
        return setting_get(session)

@admin.route('/notification', methods = ['GET', 'POST'])
def notification_admin():
    if request.method == "GET":
        return notification_get(session)
    
    if request.method == "POST":
        return notification_post(session, request)

@admin.route('/scheduler-map', methods = ['GET', 'POST'])
def scheduler_map():
    if request.method == "GET":
        return scheduler_map_get(session)
    
    if request.method == "POST":
        return scheduler_map_post(db, session, request)