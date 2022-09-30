
from . import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    type = db.Column(db.Integer, unique=False )
    content = db.Column(db.String(120), unique=False)
    time_order = db.Column(db.String(120), unique=False)

    id_receiver = db.Column(db.Integer, unique=False )
    id_sender = db.Column(db.Integer, unique=False) # nguoi tao ra product
    is_user = db.Column(db.Boolean, unique=False) # Flase: Enterprise, True: User

    status = db.Column(db.Integer, unique=False ) #0: ghi nhan, 1: chuan lap lich, 2: dang giao, 
    def __init__(self,name, type, content, time_order, id_receiver, id_sender, is_user, status) :
        self.name = name
        self.type = type
        self.content = content
        self.time_order = time_order
        self.id_receiver = id_receiver
        self.id_sender = id_sender
        self.is_user = is_user
        self.status = status

    def __repr__(self):
        return '<Order {}>'.format(self.name)  

