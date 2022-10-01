from flask import request, session
from routes import db
from application.controller.enterprise.info import info_post, info_get
from application.controller.enterprise.register import register_get
from application.controller.enterprise.logout import logout_enterprise_get
from application.controller.enterprise.revenue import revenue_get, revenue_post
from application.controller.enterprise.notification import notification_get, notification_post
from application.controller.enterprise.delivery_system import delivery_system_get, delivery_system_post
from application.controller.enterprise.product.create_product import create_product_get, create_product_post
from application.controller.enterprise.depot.create import create_depot_post, create_depot_get
from application.controller.enterprise.customer.create_customer import create_customer_post, create_customer_get
from application.controller.enterprise.order.mange_order import manage_order_get, manage_order_post
from application.controller.enterprise.order.create_order import create_order_get, create_order_post
from application.controller.enterprise.order.info import info_order_get, info_order_post

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

@enterprise.route('/notification', methods = ['GET', 'POST'])
def notification_enterprise():
    if request.method == "GET":
        return notification_get(session)
    
    if request.method == "POST":
        return notification_post(session, request)

@enterprise.route('/delivery-system', methods = ['GET', 'POST'])
def delivery_system_enterprise():
    if request.method == "GET":
        return delivery_system_get(session)
    
    if request.method == "POST":
        return delivery_system_post(session, request)

@enterprise.route('/create-depot', methods = ['GET', 'POST'])
def create_depot():
    if request.method == "GET":
        return create_depot_get(session)
    
    if request.method == "POST":
        return create_depot_post(db, session, request)

@enterprise.route('/create-customer', methods = ['GET', 'POST'])
def create_customer():
    if request.method == "GET":
        return create_customer_get(session)
    
    if request.method == "POST":
        return create_customer_post(db, session, request)

@enterprise.route('/create-product', methods = ['GET', 'POST'])
def create_product():
    if request.method == "GET":
        return create_product_get(session)
    
    if request.method == "POST":
        return create_product_post(db, session, request)

@enterprise.route('/manage-order', methods = ['GET', 'POST'])
def manage_order():
    if request.method == "GET":
        return manage_order_get(session)
    
    if request.method == "POST":
        return manage_order_post(db, session, request)

@enterprise.route('/create-order', methods = ['GET', 'POST'])
def create_order():
    if request.method == "GET":
        return create_order_get(session)
    
    if request.method == "POST":
        return create_order_post(db, session, request)

@enterprise.route('/info-order/<id_order>', methods = ['GET', 'POST'])
def info_order(id_order):
    if request.method == "GET":
        return info_order_get(session, id_order)
    
    if request.method == "POST":
        return info_order_post(db, session, request)
