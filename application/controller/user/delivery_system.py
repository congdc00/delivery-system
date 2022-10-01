from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from application.models.enterprise import Enterprise
from flask_login import current_user
from loguru import logger

def delivery_system_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_user = current_user.get_id()
            list_depot = Depot.query.filter_by(id_root = id_user , is_user = True)
            list_customer = Customer.query.filter_by(id_root = id_user, is_user = True)
            list_product = Product.query.filter_by(id_root = id_user, is_user = True)
            return render_template("user/my_service/delivery_system.html", list_depot = list_depot, list_customer = list_customer, list_product = list_product)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def delivery_system_post(session, request):
    pass