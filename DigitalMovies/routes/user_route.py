# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import Blueprint, request, render_template, make_response
import requests
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__, url_prefix='/users')

@user_blueprint.route('/register', methods=['POST'])
def register():
    return UserController.register_user(request, request.endpoint, request.method)

@user_blueprint.route('/login', methods=['POST'])
def login():
    return UserController.login_user(request, request.endpoint, request.method)

@user_blueprint.route('/logout', methods=['GET'])
def logout():
    return UserController.logout_user(request.endpoint, request.method)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    return UserController.get_users(request.endpoint, request.method)

@user_blueprint.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id, request.endpoint, request.method)

@user_blueprint.route('/<string:user_id>/edit', methods=['PUT'])
def edit_user(user_id):
    return UserController.edit_user(user_id, request, request.endpoint, request.method)

@user_blueprint.route('/<string:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id, request.endpoint, request.method)
