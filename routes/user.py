from flask import request, session
from routes import db
from application.controller.user.info import info_post, info_get
from application.controller.user.manage_enterprise import list_enterprise, login_enterprise
from application.controller.user.revenue import revenue_get, revenue_post
from application.controller.user.notification import notification_get, notification_post
from application.controller.user.delivery_system import delivery_system_get, delivery_system_post
from application.controller.user.product.create_product import create_product_get, create_product_post
from application.controller.user.depot.create_depot import create_depot_get, create_depot_post
from application.controller.user.customer.create_customer import create_customer_get, create_customer_post
from application.controller.user.order.manage_order import manage_order_get, manage_order_post
from application.controller.user.order.create_order import create_order_get, create_order_post
from application.controller.user.order.info_order import info_order_get, info_order_post
from application.controller.user.device.manage_device import get_dashboard_manager, update_list_device
from application.controller.user.device.create_device import get_form_register_device, create_new_device
from application.controller.user.warehouse.manage_warehouse import get_dashboard_warehouse, update_list_warehouse
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

@user.route('/notification', methods = ['GET', 'POST'])
def notification_user():
    if request.method == "GET":
        return notification_get(session)
    
    if request.method == "POST":
        return notification_post(session, request)

@user.route('/delivery-system', methods = ['GET', 'POST'])
def delivery_system_user():
    if request.method == "GET":
        return delivery_system_get(session)
    
    if request.method == "POST":
        return delivery_system_post(session, request)

@user.route('/create-depot', methods = ['GET', 'POST'])
def create_depot():
    if request.method == "GET":
        return create_depot_get(session)
    
    if request.method == "POST":
        return create_depot_post(db, session, request)

@user.route('/create-product', methods = ['GET', 'POST'])
def create_product():
    if request.method == "GET":
        return create_product_get(session)
    
    if request.method == "POST":
        return create_product_post(db, session, request)

@user.route('/create-customer', methods = ['GET', 'POST'])
def create_customer():
    if request.method == "GET":
        return create_customer_get(session)
    
    if request.method == "POST":
        return create_customer_post(db, session, request)

@user.route('/manage-order', methods = ['GET', 'POST'])
def manage_order():
    if request.method == "GET":
        return manage_order_get(session)
    
    if request.method == "POST":
        return manage_order_post(db, session, request)

@user.route('/create-order', methods = ['GET', 'POST'])
def create_order():
    if request.method == "GET":
        return create_order_get(session)
    
    if request.method == "POST":
        return create_order_post(db, session, request)


@user.route('/info-order/<id_order>', methods = ['GET', 'POST'])
def info_order(id_order):
    if request.method == "GET":
        return info_order_get(session, id_order)
    
    if request.method == "POST":
        return info_order_post(db, session, request)

@user.route('/manage-device', methods = ['GET', 'POST'])
def manage_device():
    if request.method == "GET":
        return get_dashboard_manager(session)
    
    if request.method == "POST":
        return update_list_device()

@user.route('/create-device', methods = ['GET', 'POST'])
def create_device():
    if request.method == "GET":
        return get_form_register_device()
    
    if request.method == "POST":
        return create_new_device(db, request)

@user.route('manage-warehouse', methods = ['GET', 'POST'])
def manage_warehouse():
    if request.method == "GET":
        return get_dashboard_warehouse()
    
    if request.method == "POST":
        return update_list_warehouse() 
