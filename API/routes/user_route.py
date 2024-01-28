# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import Blueprint, request, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__, url_prefix='/users')

@user_blueprint.route('/register', methods=['POST'])
@jwt_required(optional=True)  # Vérifie la présence du jeton sans bloquer la route
def register():
    return UserController.register_user(request.json)

@user_blueprint.route('/login', methods=['POST'])
@jwt_required(optional=True)  # Vérifie la présence du jeton sans bloquer la route
def login():
    return UserController.login_user()

@user_blueprint.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    return UserController.logout_user()

@user_blueprint.route('/', methods=['GET'])
@jwt_required()
def get_users():
    return UserController.get_users()

@user_blueprint.route('/<string:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return UserController.get_user(user_id)

@user_blueprint.route('/<string:user_id>/edit', methods=['PUT'])
@jwt_required()
def edit_user(user_id):
    return UserController.edit_user(user_id, request.json)

@user_blueprint.route('/<string:user_id>/deactivate', methods=['DELETE'])
@jwt_required()
def deactivate_user(user_id):
    return UserController.deactivate_user(user_id)

@user_blueprint.route('/<string:user_id>/delete', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return UserController.delete_user(user_id)