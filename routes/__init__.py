# Thiet lap cac dieu huong cho server
from app import app, db
from application.models.user import User
from flask_login import LoginManager
from routes.authentication import authentication
from routes.admin import admin
from routes.user import user
from routes.enterprise import enterprise

login_manager = LoginManager(app = app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(authentication, url_prefix = "/")
app.register_blueprint(admin, url_prefix = "/admin")
app.register_blueprint(user, url_prefix = "/user")
app.register_blueprint(enterprise, url_prefix = "/enterprise")