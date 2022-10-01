from flask import render_template, redirect, url_for
from application.models.depot import Depot
from application.models.o2p import O2P
from application.models.product import Product
from application.models.customer import Customer
from application.models.order import Order
from flask_login import current_user
from flask import flash
from loguru import logger
from datetime import datetime
def info_order_get(session,id_order):
    if current_user.is_authenticated:
        if session['type'] == 2:

            id= int(id_order)
            order  = Order.query.filter_by(id = id).first()
            id_receiver= order.id_receiver
            receiver = Customer.query.filter_by(id = id_receiver).first()
            name_receiver = receiver.name
            list_product = O2P.query.filter_by(id_order = id)

            #user
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
            

            return render_template("enterprise/order/info.html", list_result = list_result)

    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
    
   
def info_order_post(db, session, request):
    pass