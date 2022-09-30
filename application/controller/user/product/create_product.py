from flask import render_template, redirect, url_for,flash
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from application.helper.check_session import get_type_session
from loguru import logger

def create_product_get(session):
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
        return render_template("user/product/create_product.html", admin = admin, session_key = session_key, list_depot= list_depot)
    
    #enterprise
    else: 
        id = session['enterprise']
        enterprise = Enterprise.query.filter_by(id = id).first()
        list_depot = Depot.query.filter_by(id_root = id , is_user = False)
        return render_template("user/product/create_product.html", admin = admin, session_key = session_key, enterprise = enterprise, list_depot = list_depot)

def create_product_post(db, session, request):
    nameProduct = request.form["nameProduct"]
    idProduct = request.form['idProduct']
    id_depot = int(request.form['idDepot'])
    
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

    if nameProduct and idProduct and id_depot:
            new_product = Product(name = nameProduct, id_product = idProduct,weight = 0, id_deport = id_depot, id_root = id_root, is_user= is_user)
            db.session.add(new_product)
            db.session.commit()
            flash(message = "Bạn đã tạo sản phẩm thành công!", category = "info")
            logger.info("Add new product")

    return render_template("user/product/create_product.html", session_key = session_key, admin = admin)