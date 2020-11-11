from .app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

'''
Keeps track of the logged in user and reference it by the user ID 
'''


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))


'''
creates a table for Users data
Id: is row number
BMIs: is the refrence for the BMI table
measurement: measurement to be uploaded
'''


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    BMIs = db.relationship('BMI', backref='user', lazy=True)
    calories = db.relationship('Calorie', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


''' 
creates a table for BMI data
measurement: BMI data to be uploaded to the table 
date: automatically updates the time and date of the uploaded data
user_id: references the id of the user who uploaded the data
'''


class BMI(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    measurement = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"BMI({self.date}, {self.measurement})"


'''
creates a table for calorie data
measurement: measurement to be uploaded
date: automatically updates the time and date of the uploaded data
user_id: references the id of the user who uploaded the data
'''


class Calorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    measurement = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Calorie({self.date}, {self.measurement})"
