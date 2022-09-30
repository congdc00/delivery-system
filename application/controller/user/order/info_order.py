from itertools import product
from math import prod
from xml.dom.minidom import Identified
from flask import render_template, redirect, url_for,flash
from application.models.customer import Customer
from application.models.user import User
from application.models.o2p import O2P
from application.models.order import Order
from application.models.product import Product
from application.models.depot import Depot
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def info_order_get(session,id_order):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    id= int(id_order)
    order  = Order.query.filter_by(id = id).first()
    id_receiver= order.id_receiver
    receiver = Customer.query.filter_by(id = id_receiver).first()
    name_receiver = receiver.name

    list_product = O2P.query.filter_by(id_order = id)
    #User
    if type == 1 : 
        list_result = []
        for product_tmp in list_product:
            id_product = product_tmp.id_product
            product = Product.query.filter_by(id = id_product).first()
            name_product =product.name
            number = product_tmp.number
            id_deport = product.id_deport
            deport = Depot.query.filter_by(id = id_deport).first()
            name_deport = deport.name
            list_result.append([id_product, name_product, number, name_deport])

        
        return render_template("user/order/info_order.html", admin = admin, session_key = session_key,name_receiver =name_receiver,  list_result= list_result)
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()

        return render_template("user/order/info_order.html", admin = admin, session_key = session_key, enterprise = enterprise, list_product = list_product)

def info_order_post(db, session, request):
    pass