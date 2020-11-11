from .app import db, login_manager
from datetime import datetime
from flask_login import UserMixin

'''
Keeps track of the logged in user and reference it by the user ID 
'''


@login_manager.user_loader
def loader_user(user_id):
    return User.query.get(int(user_id))

<<<<<<< HEAD

'''
creates a table for Users data
Id: is row number
BMIs: is the refrence for the BMI table
measurement: measurement to be uploaded
'''


=======
# creates a table for Users data
# Id: is row number
# BMIs: is the reference for the BMI table
# measurement: measurement to be uploaded
>>>>>>> story/4pt3
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    BMIs = db.relationship('BMI', backref='user', lazy=True)
<<<<<<< HEAD
    calories = db.relationship('Calorie', backref='user', lazy=True)
=======
    nutrition_intake = db.relationship('Nutrition', backref='user',lazy=True)
>>>>>>> story/4pt3

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


# Forum


class Forum(db.Model):
    post_id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)


class Thread(db.Model):
    post_id = db.Column(db.Integer, nullable=False, primary_key=True)
    thread_id = db.Column(db.Integer, nullable=False, unique=False)


class Post(db.Model):
    post_id = db.Column(db.Integer, nullable=False, primary_key=True)
    time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.UnicodeText, nullable=False)

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

# creates a table for user nutrition data
class Nutrition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable = False)
    calories = db.Column(db.Integer, nullable=False)
    fat = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    protein = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Nutrition({self.description}, {self.calories}, {self.fat}, {self.carbs}, {self.protein})"

