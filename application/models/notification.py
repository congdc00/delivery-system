
from . import db

class Notification(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=False)
    content = db.Column(db.String(500), unique=False)
    time = db.Column(db.String(120), unique=False)
    id_sender = db.Column(db.Integer, unique=False)
    id_receiver = db.Column(db.Integer, unique=False)
    type = db.Column(db.Integer, unique=False)

    def __init__(self, title, content, time, id_sender, id_receiver, type) :

        self.title = title
        self.content = content
        self.time = time
        self.id_sender = id_sender
        self.id_receiver = id_receiver
        self.type = type

    def __repr__(self):
        return '<Notification {}>'.format(self.title)  

