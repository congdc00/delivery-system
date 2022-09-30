from itertools import product
from flask import render_template, redirect, url_for,flash
from application.models.user import User
from application.models.order import Order
from application.models.o2p import O2P
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger
from datetime import datetime

def create_order_get(session):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    
    if 'list_id_product' in session:
        #User
        if type == 1 : 
            user = User.query.filter_by(email = session_key).first()
            id_user = int(user.id)
            list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
            return render_template("user/order/create_order_2.html", admin = admin, session_key = session_key, list_customer =list_customer)
        
        #enterprise
        else: 
            id = session['enterprise']
            enterprise = Enterprise.query.filter_by(id = id).first()
            list_customer = Customer.query.filter_by(id_root = id, is_user = False)
            return render_template("user/order/create_order_2.html", admin = admin, session_key = session_key, enterprise = enterprise, list_customer =list_customer)

    else:
        #User
        if type == 1 : 
            user = User.query.filter_by(email = session_key).first()
            id_user = int(user.id)
            list_product = Product.query.filter_by(id_root = id_user, is_user = True)
            return render_template("user/order/create_order_1.html", admin = admin, session_key = session_key, list_product = list_product)
        
        #enterprise
        else: 
            id = session['enterprise']
            enterprise = Enterprise.query.filter_by(id = id).first()
            list_product = Product.query.filter_by(id_root = id, is_user = False)
            return render_template("user/order/create_order_1.html", admin = admin, session_key = session_key, enterprise = enterprise, list_product = list_product)

        
def create_order_post(db, session, request):

    
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    

    
    if 'list_id_product' in session:
        list_id_product = session['list_id_product'] 
        list_number_product = session['list_number_product']

        name = request.form['nameOrder']
        order_type = request.form['type']
        print(f'order type {order_type}')
        content = request.form['content']
        time = datetime.now()
        time_order =  time.strftime("%d/%m/%Y %H:%M:%S")
        id_receiver = request.form['customer']


        flash(message = "Tạo đơn thành công!", category = "info")
        #User
        if type == 1 : 
            user = User.query.filter_by(email = session_key).first()
            id_sender = user.id
            is_user = True
            status = 0
            new_order = Order(name =name , type = order_type, content = content, time_order = time_order, id_receiver = id_receiver, id_sender = id_sender, is_user = is_user, status = status)
            db.session.add(new_order)
            db.session.commit()
            id_order = int(new_order.id)

            for id_product, number in zip(list_id_product, list_number_product):
                new_record = O2P(id_order=id_order, id_product= id_product, number=number)
                db.session.add(new_record)

            db.session.commit()
            session.pop("list_id_product", None)
            session.pop("list_number_product", None)
            return render_template("user/order/create_order_2.html", session_key = session_key, admin = admin)
        #enterprise
        else: 
            id = session['enterprise']
            enterprise = Enterprise.query.filter_by(id = id).first()
            is_user = False
            status = 0
            new_order = Order(name =name , type = order_type, content = content, time_order = time_order, id_receiver = id_receiver, id_sender = id, is_user = is_user, status = status)
        
            db.session.add(new_order)
            db.session.commit()
            id_order = int(new_order.id)

            for id_product, number in zip(list_id_product, list_number_product):
                new_record = O2P(id_order=id_order, id_product= id_product, number=number)
                db.session.add(new_record)

            db.session.commit()

            session.pop("list_id_product", None)
            session.pop("list_number_product", None)
            return render_template("user/order/create_order_2.html", session_key = session_key, admin = admin, enterprise = enterprise)
       
    else:
        
        list_checkbox = request.form.getlist("checkbox")
        list_id_product = []
        list_number_product = []
        for checkbox in list_checkbox:
            list_id_product.append(checkbox)
            name_input = checkbox+'_number'
            number = request.form[name_input]
            list_number_product.append(number)
        
        session['list_id_product'] = list_id_product
        session['list_number_product'] = list_number_product


        #User
        if type == 1 : 
            user = User.query.filter_by(email = session_key).first()
            id_user = int(user.id)
            list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
            return render_template("user/order/create_order_2.html", admin = admin, session_key = session_key, list_customer =list_customer)
        
        #enterprise
        else: 
            id = session['enterprise']
            enterprise = Enterprise.query.filter_by(id = id).first()
            list_customer = Customer.query.filter_by(id_root = id, is_user = False)
            return render_template("user/order/create_order_2.html", admin = admin, session_key = session_key, enterprise = enterprise, list_customer =list_customer)
