
from . import db

class Device(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    type = db.Column(db.Integer, unique=False)
    info = db.Column(db.String(120), unique=False)
    limit_weight = db.Column(db.Integer, unique=False)
    made_by = db.Column(db.String(30), unique=False)
    made_in = db.Column(db.String(30), unique=False)

    status = db.Column(db.Integer, unique=False) # trang thai hoat dong

    money = db.Column(db.Integer, unique=False)
    available = db.Column(db.Boolean, unique=False)
    id_root = db.Column(db.Integer, unique=False) # nguoi tao ra product
    is_user = db.Column(db.Boolean, unique=False) # Flase: Enterprise, True: User
    

    def __init__(self, name, type, info,limit_weight,made_by,made_in,status,available,money, id_root, is_user) :
        self.name = name
        self.type = type
        self.info = info
        self.limit_weight = limit_weight
        self.made_by = made_by
        self.made_in = made_in
        self.status = status
        self.available = available
        self.money = money
        self.id_root = id_root
        self.is_user = is_user

    def __repr__(self):
        return '<Device {}>'.format(self.name)  

