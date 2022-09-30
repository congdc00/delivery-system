
from . import db

class Depot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    address = db.Column(db.String(120), unique=False)
    phone_num = db.Column(db.String(10), unique=False)

    id_root = db.Column(db.Integer, unique=False) # nguoi tao ra product
    is_user = db.Column(db.Boolean, unique=False) # Flase: Enterprise, True: User
    

    def __init__(self, name, address, phone_num, id_root, is_user) :

        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.id_root = id_root
        self.is_user = is_user

    def __repr__(self):
        return '<Depot {}>'.format(self.name)  

