from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False)

    meals = db.relationship("Meals", backref="user", cascade="all, delete-orphan")
    favorites = db.relationship("Favorites", backref="user", cascade="all, delete-orphan")

class Meals(db.Model):
    __tablename__ = "meals"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    recipe_name = db.Column(db.Text, nullable=False)
    recipe_desc = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
class Favorites(db.Model):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.Text, nullable=False)
    recipe_name = db.Column(db.Text, nullable=False)
    recipe_desc = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    