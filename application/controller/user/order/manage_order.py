from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from application.models.order import Order
from flask_login import current_user
from flask import flash
from loguru import logger

def manage_order_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_user = current_user.get_id()
            list_order = Order.query.filter_by(id_sender = id_user , is_user = True)
            return render_template("user/my_order/manage_order.html", list_order= list_order)
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
        
def manage_order_post(db, session, request):
    pass