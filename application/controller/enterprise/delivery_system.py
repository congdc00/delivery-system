from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.product import Product
from flask_login import current_user
from loguru import logger

def delivery_system_get(session):
    if current_user.is_authenticated:
        if session['type'] == 2:
            id_enterprise = session['id_enterprise']
            list_depot = Depot.query.filter_by(id_root = id_enterprise , is_user = False)
            list_customer = Customer.query.filter_by(id_root = id_enterprise, is_user = False)
            list_product = Product.query.filter_by(id_root = id_enterprise, is_user = False)
            return render_template("enterprise/delivery_system.html", list_depot = list_depot, list_customer = list_customer, list_product = list_product)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
        
def delivery_system_post(session, request):
    pass