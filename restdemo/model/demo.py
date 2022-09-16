from restdemo import db

class Demo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    mobile = db.Column("mobile", db.String(64))

def __init__(self, username, age, mobile):
    self.username = username
    self.age = age
    self.mobile = mobile