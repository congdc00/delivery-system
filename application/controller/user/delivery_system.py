from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def delivery_system_get(session):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    
    #User
    if type == 1 : 
        
        user = User.query.filter_by(email = session_key).first()
        id_user = int(user.id)
        list_depot = Depot.query.filter_by(id_root = id_user , is_user = True)
        list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
        list_product = Product.query.filter_by(id_root = id_user, is_user = True)
        return render_template("user/delivery_system.html", admin = admin, session_key = session_key, list_depot = list_depot, list_customer = list_customer, list_product = list_product)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        list_depot = Depot.query.filter_by(id_root = id , is_user = False)
        list_customer = Customer.query.filter_by(id_root = id, is_user = False)
        list_product = Product.query.filter_by(id_root = id, is_user = False)
        return render_template("user/delivery_system.html", admin = admin, session_key = session_key, enterprise = enterprise, list_depot = list_depot, list_customer = list_customer, list_product = list_product)

def delivery_system_post(session, request):
    pass