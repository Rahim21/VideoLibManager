# routes/user_route.py
from flask import Blueprint, request
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users/register', methods=['POST'])
def register_user():
    user_data = request.json
    return UserController.register_user(user_data)

@user_blueprint.route('/users/login', methods=['POST'])
def login():
    return UserController.login()

@user_blueprint.route('/users/logout', methods=['GET'])
def logout():
    return UserController.logout()

@user_blueprint.route('/users', methods=['GET'])
def get_users():
    return UserController.get_users()

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id)

@user_blueprint.route('/users/edit/<int:user_id>', methods=['PUT'])
def edit_user(user_id):
    updated_data = request.json
    return UserController.edit_user(user_id, updated_data)

@user_blueprint.route('/users/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return UserController.delete_user(user_id)
