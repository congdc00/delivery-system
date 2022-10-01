from symbol import import_from
from flask import render_template, redirect, url_for
from application.helper.check.check_login import check_login
from application.models.device import Device
from flask_login import current_user
from flask import request
from flask import flash
from loguru import logger

def get_form_register_device():
    if check_login("user"):
        return render_template("user/my_device/create_device.html")
    else:
        return redirect(url_for("index"))

def create_new_device(db, request):
    name_device = request.form["name_device"]
    type = int(request.form['type'])
    info = request.form['info']
    limit_weight = int(request.form['limit_weight'])
    made_by = request.form['made_by']
    made_in = request.form['made_in']

    id_root = int(current_user.get_id())
    is_user = True
    if check_login("user"):
        if name_device and limit_weight:
            new_product = Device(name= name_device, type=type, info=info,limit_weight=limit_weight,made_by=made_by,made_in = made_in,status = 0,available = False,money = 0 , id_root = id_root, is_user = is_user)
            db.session.add(new_product)
            db.session.commit()
            flash(message = "Bạn đã thêm thiết bị thành công!", category = "info")
            logger.info("Add new product")

            return redirect(url_for("user.manage_device"))
        else:
            flash(message = "Kiểm tra lại các thông tin!", category = "error")
            return render_template("user/my_device/create_device.html")
    
    else:
        return redirect(url_for("index"))
    