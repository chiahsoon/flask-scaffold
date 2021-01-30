import secrets

from flask import Flask
from flask_cors import CORS

from configurations.configs import configs  # Flask App Config
from controllers import user_controller, home_controller
from utilities.extensions import db


def register_routes(app_obj):
    app_obj.register_blueprint(home_controller, url_prefix="/")
    app_obj.register_blueprint(user_controller, url_prefix="/")


def create_app(name):

    # Setup Flask
    app_obj = Flask(name)
    app_obj.app_context().push()
    app_obj.config['SQLALCHEMY_DATABASE_URI'] = configs.get_database_url()
    app_obj.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app_obj.secret_key = secrets.token_urlsafe(32)
    register_routes(app_obj)

    # Initialise ORM
    db.init_app(app_obj)
    db.create_all()

    # Allow CORS
    CORS(app_obj)

    return app_obj


app = create_app(__name__)
