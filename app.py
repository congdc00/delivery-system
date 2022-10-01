from loguru import logger
from flask_migrate import Migrate
from flask import Flask
from config import TEMPLATE_FOLDER, TIME_SESSION
from config.config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

    

# Khoi tao Flask server 
app = Flask(__name__, template_folder= TEMPLATE_FOLDER)

# Apply flask cors de moi domain khac deu goi duoc
CORS(app = app, origins='*')

# config
app.config.from_object(Config)
app.permanent_session_lifetime = TIME_SESSION


# khoi tao database
db = SQLAlchemy(app=app)

#migrate
migrate = Migrate(app, db)

import routes

from application.models import order, user, customer, product, enterprise, e2u, notification, depot, o2p, device

if __name__ == "__main__":

    from routes.routes import app as server

    server.run(debug=True, host="0.0.0.0", port="9999")