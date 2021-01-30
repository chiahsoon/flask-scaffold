import uuid

from models import User
from datetime import datetime
from werkzeug.exceptions import Conflict, BadRequest, Unauthorized

from utilities.extensions import db


class UserService:

    @staticmethod
    def create_user(username, email, password, name):
        if User.query.filter_by(username=username).first():
            raise Conflict("UserService :: create_user :: Username already exists.")

        current_time = datetime.now()
        new_user = User(id=str(uuid.uuid4()), username=username, email=email,
                        password=password, name=name, created_at=current_time, updated_at=current_time)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()

    @staticmethod
    def get_user_by_id(id):
        found_user = User.query.filter_by(id=id).first()
        if not found_user:
            raise BadRequest("UserService :: get_user_by_id :: There is no valid current user.")
        return found_user.to_dict()

    @staticmethod
    def login(username, password):
        found_user = User.query.filter_by(username=username, password=password).first()
        if not found_user:
            raise Unauthorized("UserService :: signin_user :: The login credentials are invalid.")
        return found_user.to_dict()
