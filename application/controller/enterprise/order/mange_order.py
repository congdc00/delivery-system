from flask import render_template, redirect, url_for
from application.models.order import Order
from flask_login import current_user
from flask import flash
from loguru import logger

def manage_order_get(session):
    if current_user.is_authenticated:
        if session['type'] == 2:
            id_enterprise = session['id_enterprise']
            list_order = Order.query.filter_by(id_sender = id_enterprise , is_user = False)
            return render_template("enterprise/order/manage.html", list_order= list_order)
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
        
def manage_order_post(db, session, request):
    pass