
from flask import request, redirect, url_for, render_template, session,flash
from . import app
from app import db
from application.controller.user.revenue import revenue_get, revenue_post
from application.controller.notification import notification_get, notification_post
from application.controller.user.delivery_system import delivery_system_get, delivery_system_post
from application.controller.user.depot.create_depot import create_depot_get, create_depot_post
from application.controller.user.customer.create_customer import create_customer_get, create_customer_post
from application.controller.user.product.create_product import create_product_get, create_product_post
from application.controller.user.order.manage_order import manage_order_get, manage_order_post
from application.controller.user.order.create_order import create_order_get, create_order_post
from application.controller.user.order.info_order import info_order_get, info_order_post 
from application.controller.admin.scheduler_map import scheduler_map_get, scheduler_map_post
from application.controller.index import index_get





@app.route('/', methods = ['POST', 'GET'])
def index():
    return index_get(session)





@app.route('/logout-enterprise', methods = ['GET', 'POST'])
def logout_enterprise():
    if request.method == "GET":
        if "enterprise" in session:
            session.pop("enterprise", None)
            return redirect(url_for('index'))

@app.route('/revenue', methods = ['GET', 'POST'])
def revenue():
    if request.method == "GET":
        return revenue_get(session)
    
    if request.method == "POST":
        return revenue_post(session, request)

@app.route('/notification', methods = ['GET', 'POST'])
def notification():
    if request.method == "GET":
        return notification_get(session)
    
    if request.method == "POST":
        return notification_post(session, request)

@app.route('/delivery-system', methods = ['GET', 'POST'])
def delivery_system():
    if request.method == "GET":
        return delivery_system_get(session)
    
    if request.method == "POST":
        return delivery_system_post(session, request)

@app.route('/create-depot', methods = ['GET', 'POST'])
def create_depot():
    if request.method == "GET":
        return create_depot_get(session)
    
    if request.method == "POST":
        return create_depot_post(db, session, request)

@app.route('/create-customer', methods = ['GET', 'POST'])
def create_customer():
    if request.method == "GET":
        return create_customer_get(session)
    
    if request.method == "POST":
        return create_customer_post(db, session, request)

@app.route('/create-product', methods = ['GET', 'POST'])
def create_product():
    if request.method == "GET":
        return create_product_get(session)
    
    if request.method == "POST":
        return create_product_post(db, session, request)

@app.route('/manage-order', methods = ['GET', 'POST'])
def manage_order():
    if request.method == "GET":
        return manage_order_get(session)
    
    if request.method == "POST":
        return manage_order_post(db, session, request)

@app.route('/create-order', methods = ['GET', 'POST'])
def create_order():
    if request.method == "GET":
        return create_order_get(session)
    
    if request.method == "POST":
        return create_order_post(db, session, request)

@app.route('/api/create-order', methods = ['GET', 'POST'])
def api_create_order():
    if request.method == "GET":
        return create_order_get(session)
    
    if request.method == "POST":
        return create_order_post(db, session, request)


@app.route('/info-order/<id_order>', methods = ['GET', 'POST'])
def info_order(id_order):
    if request.method == "GET":
        return info_order_get(session, id_order)
    
    if request.method == "POST":
        return info_order_post(db, session, request)

@app.route('/scheduler-map', methods = ['GET', 'POST'])
def scheduler_map():
    if request.method == "GET":
        return scheduler_map_get(session)
    
    if request.method == "POST":
        return scheduler_map_post(db, session, request)
# @app.route('/add', methods = ['POST', 'GET'])
# @cross_origin(origins='*')
# def add():
#     a = request.form.get("a")
#     b = request.form.get("b")
#     result = int(a) + int(b)
#     return "Ham cong = " + str(result)
    


