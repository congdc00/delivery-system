from flask import render_template, redirect, url_for,flash
from application.models.order import Order
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def scheduler_map_get(session):
    type = get_type_session(session)

    if type != 0 :
        return redirect(url_for("index"))
    else:
    
        session_key = session['session_key']
        admin = session['admin']
        return render_template("admin/scheduler_map.html", session_key = session_key, admin = admin)
    

def scheduler_map_post(db, session, request):
    pass