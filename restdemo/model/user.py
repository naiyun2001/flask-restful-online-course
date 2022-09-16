from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
# import jwt
# from datetime import datetime, timedelta
# from flask import current_app

from restdemo import db
from restdemo.model.base import Base


class User(Base):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)

    tweet = relationship("Tweet")

    def __repr__(self):
        return "id={}, username={}".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    '''
    jwt 產生 token

    def generate_token(self):
        # 產生 token
        try:
            # 要 encode 的 JSON
            payload = {
                "exp": datetime.utcnow() + timedelta(minutes=5),    # timeout 的時間
                "iat": datetime.utcnow(),                           # 規範 toke 當前時間，不產生未來的 token
                "sub": self.username
            }
            # create token
            jwt_token = jwt.encode(
                payload,
                current_app.config.get("SECRET_KEY"),
                algorithm = "HS256"
            )
            return jwt_token

        except Exception as e:
            # return an error in string if an exception occurs
            return str(e)
    '''

    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(User.username == username).first()

    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            # check password
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload["identity"]
        user = User.get_by_id(user_id)
        return user
