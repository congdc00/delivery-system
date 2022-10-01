from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from flask_login import current_user
from flask import flash
from loguru import logger

def create_product_get(session):
    if current_user.is_authenticated:
        if session['type'] == 2:
            id_enterprise = session['id_enterprise']
            list_depot = Depot.query.filter_by(id_root = id_enterprise , is_user = False)
            return render_template("enterprise/product/create_product.html", list_depot= list_depot)
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def create_product_post(db, session, request):
    nameProduct = request.form["nameProduct"]
    idProduct = request.form['idProduct']
    id_depot = int(request.form['idDepot'])

    if current_user.is_authenticated:
        if session['type'] == 2:
            id_root = session['id_enterprise']
            is_user = False
            
            if nameProduct and idProduct and id_depot:
                new_product = Product(name = nameProduct, id_product = idProduct,weight = 0, id_deport = id_depot, id_root = id_root, is_user= is_user)
                db.session.add(new_product)
                db.session.commit()
                flash(message = "Bạn đã tạo sản phẩm thành công!", category = "info")
                logger.info("Add new product")

                return render_template("enterprise/product/create_product.html")
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))