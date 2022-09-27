
from . import db

class Enterprise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False)
    tax_id_number =  db.Column(db.String(120), unique=False)
    money = db.Column(db.Integer, unique=False )
    logo_path = db.Column(db.String(120), unique=False)

    def __init__(self, name, tax_id_number, money, logo_path) :

        self.name = name
        self.tax_id_number = tax_id_number
        self.money = money
        self.logo_path = logo_path

    def __repr__(self):
        return '<Enterprise {}>'.format(self.name)  

