from flask_login import current_user
from flask import session

def check_login(type_target):

    if current_user.is_authenticated:
        if session['type'] == 0:
            if type_target == "admin":
                return True
            else:
                return False

        if session['type'] == 1:
            if type_target == "user":
                return True
            else:
                return False
        
        if session['type'] == 2:
            if type_target == "enterprise":
                return True
            else:
                return False
    else:
        if type_target == "guest":
            return True
        else:
            return False
    