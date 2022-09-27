

class Config(object):
    CORS_HEADERS = 'Content-Type'
    SECRET_KEY = 'dinhchicongf9'
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:Dinhchicong123.@localhost:5432/delivery_system'
    SQLALCHEMY_TRACK_MODIFICATIONS = False