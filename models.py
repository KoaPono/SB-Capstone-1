from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.Text, nullable=False, unique=True)
    username = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text,nullable=False)

    meals = db.relationship("Meals", backref="user", cascade="all, delete-orphan")
    favorites = db.relationship("Favorites", backref="user", cascade="all, delete-orphan")

    @classmethod
    def signup(cls, username, email, password, image_url):
        """Signs up user, Hashes password and adds user to system."""

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
        )

        db.session.add(user)
        return user
    
    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password` return user if found, else return False."""

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False

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
    
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)