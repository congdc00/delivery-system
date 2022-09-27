
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(80), unique=False)

    username = db.Column(db.String(80), unique=False)
    id_card = db.Column(db.String(20), unique=True)
    dob = db.Column(db.String(20), unique=False)
    sex = db.Column(db.String(20), unique=False)
    nationality = db.Column(db.String(20), unique=False)
    place_of_origin = db.Column(db.String(80), unique=False)
    place_of_recidence = db.Column(db.String(80), unique=False)
    date_of_expiry = db.Column(db.String(80), unique=False)
    tax_id_number = db.Column(db.String(20), unique=True)
    admin = db.Column(db.Boolean, unique=False, default=False)
    money = db.Column(db.Integer, unique=False)

    def __init__(self, email, phone_number, password, username, id_card, dob, sex, nationality, place_of_origin, place_of_recidence, date_of_expiry, tax_id_number) :

        self.email = email
        self.phone_number = phone_number
        self.password = password

        self.username = username
        self.id_card = id_card
        self.dob = dob
        self.sex = sex
        self.nationality = nationality
        self.place_of_origin = place_of_origin
        self.place_of_recidence = place_of_recidence
        self.date_of_expiry = date_of_expiry

        self.tax_id_number = tax_id_number

    def __repr__(self):
        return '<User {}>'.format(self.username)  

