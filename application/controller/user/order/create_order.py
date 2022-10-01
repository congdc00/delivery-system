from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.o2p import O2P
from application.models.product import Product
from application.models.customer import Customer
from application.models.order import Order
from application.models.enterprise import Enterprise
from flask_login import current_user
from flask import flash
from loguru import logger
from datetime import datetime

def create_order_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:

            id_user = current_user.get_id()
            
            if 'list_id_product' in session:
                list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
                return render_template("user/my_order/create_order_2.html",list_customer =list_customer)
                
            else:
                
                list_product = Product.query.filter_by(id_root = id_user, is_user = True)
                return render_template("user/my_order/create_order_1.html", list_product = list_product)
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
    
    
def create_order_post(db, session, request):
    if current_user.is_authenticated:
        if session['type'] == 1:

            #step 2
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
                
                id_sender = current_user.get_id()
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
                return render_template("user/my_order/create_order_2.html")
            
            #step 1
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


                
                id_user = current_user.get_id()
                list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
                return render_template("user/my_order/create_order_2.html", list_customer =list_customer)
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
    
    