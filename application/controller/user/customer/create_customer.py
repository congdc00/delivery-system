from flask import render_template, redirect, url_for
from application.models.user import User
from application.models.depot import Depot
from application.models.customer import Customer
from flask_login import current_user
from flask import flash
from loguru import logger


def create_customer_get(session):
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_user = current_user.get_id()
            list_depot = Depot.query.filter_by(id_root = id_user , is_user = True)
            return render_template("user/my_service/customer/create_customer.html", list_depot= list_depot)
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

def create_customer_post(db, session, request):
    name = request.form["name"]
    address = request.form['address']
    phoneNum = request.form['phoneNum']
    
    if current_user.is_authenticated:
        if session['type'] == 1:
            id_root = current_user.get_id()
            is_user = True
            if name and phoneNum and address:
                new_depot = Customer( name = name, address = address, phone_num = phoneNum, path_face_id = "", weight = 0, upper_bound = 0, lower_bound=0, id_root = id_root, is_user= is_user)
                db.session.add(new_depot)
                db.session.commit()
                flash(message = "Bạn đã tạo khách hàng thành công!", category = "info")
                logger.info("Add new depot")
                return render_template("user/my_service/customer/create_customer.html")
    
        else:
            return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

   

    
   