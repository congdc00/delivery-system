from flask import render_template, redirect, url_for,flash
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def create_customer_get(session):
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    
    #User
    if type == 1 : 
        
        user = User.query.filter_by(email = session_key).first()

        return render_template("user/customer/create_customer.html", admin = admin, session_key = session_key)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        return render_template("user/customer/create_customer.html", admin = admin, session_key = session_key, enterprise = enterprise)

def create_customer_post(db, session, request):
    name = request.form["name"]
    address = request.form['address']
    phoneNum = request.form['phoneNum']
    
    type = get_type_session(session)

    if type == 3 or type == 0:
        return redirect(url_for("index"))
    
    
    session_key = session['session_key']
    admin = session['admin']
    
    #User
    if type == 1 : 
        
        user = User.query.filter_by(email = session_key).first()
        id_root = user.id
        is_user = True
    
    #enterprise
    else: 
        id_root = session['enterprise']
        is_user = False

    if name and phoneNum and address:
            new_depot = Customer( name = name, address = address, phone_num = phoneNum, path_face_id = "", weight = 0, upper_bound = 0, lower_bound=0, id_root = id_root, is_user= is_user)
            db.session.add(new_depot)
            db.session.commit()
            flash(message = "Bạn đã tạo khách hàng thành công!", category = "info")
            logger.info("Add new depot")

    return render_template("user/depot/create_depot.html", session_key = session_key, admin = admin)