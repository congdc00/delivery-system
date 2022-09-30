from flask import render_template, redirect, url_for,flash
from application.models.order import Order
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def manage_order_get(session):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    
    #User
    if type == 1 : 
        
        user = User.query.filter_by(email = session_key).first()
        id_user = int(user.id)
        list_order = Order.query.filter_by(id_sender = id_user , is_user = True)
        print(list_order)
        return render_template("user/order/manage_order.html", admin = admin, session_key = session_key, list_order = list_order)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        list_order = Order.query.filter_by(id_sender = id , is_user = False)
        return render_template("user/order/manage_order.html", admin = admin, session_key = session_key, enterprise = enterprise, list_order = list_order)

def manage_order_post(db, session, request):
    pass