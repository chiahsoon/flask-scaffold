from flask import Blueprint, jsonify, request, session
from werkzeug.exceptions import Unauthorized, BadRequest
from services import UserService
from views import RestResponse
from errors import GenericException
from utilities import SESSION_USER_ID_KEY

user_controller = Blueprint("controllers/user_controller", __name__)


@user_controller.before_request
def require_login():
    endpoint = request.endpoint.split(".")[-1]
    allowed_routes = ['login', 'signup']
    if endpoint not in allowed_routes and SESSION_USER_ID_KEY not in session:
        response = RestResponse()
        response.data = GenericException(message="Authentication is required.").to_dict()
        return jsonify(response.to_dict()), 401


@user_controller.route('/signup', methods=['POST'])
def signup():
    response = RestResponse()
    try:
        if request.method == "POST":
            data = request.get_json()
            newly_created_user = UserService.create_user(data.get("username"), data.get("email"),
                                                         data.get("password"), data.get("name"))
            response.data = newly_created_user
        return jsonify(response.to_dict())
    except BadRequest as err:
        response.data = GenericException(message=err.description).to_dict()
        return jsonify(response.to_dict()), err.code


@user_controller.route('/login', methods=['POST'])
def login():
    response = RestResponse()
    try:
        if request.method == "POST":
            data = request.get_json()
            current_user = UserService.login(username=data.get("username"), password=data.get("password"))
            response.data = current_user
            session[SESSION_USER_ID_KEY] = current_user["id"]
        return jsonify(response.to_dict())
    except Unauthorized as err:
        response.data = GenericException(message=err.description).to_dict()
        return jsonify(response.to_dict()), err.code


@user_controller.route('/logout', methods=['GET'])
def logout():
    response = RestResponse()
    try:
        if request.method == "GET":
            current_user_id = session[SESSION_USER_ID_KEY]
            current_user = UserService.get_user_by_id(current_user_id)
            response.data = current_user
            del session[SESSION_USER_ID_KEY]
        return jsonify(response.to_dict()), 200
    except BadRequest as err:
        response.data = GenericException(message=err.description)
        return jsonify(response.to_dict()), err.code


@user_controller.route('/current_user', methods=['GET'])
def get_current_user():
    response = RestResponse()
    try:
        if request.method == "GET":
            current_user_id = session[SESSION_USER_ID_KEY]
            current_user = UserService.get_user_by_id(current_user_id)
            response.data = current_user
        return jsonify(response.to_dict()), 200
    except BadRequest as err:
        response.data = GenericException(message=err.description).to_dict()
        return jsonify(response.to_dict()), err.code
