# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import Blueprint, request, redirect, url_for
from flask_jwt_extended import jwt_required, get_jwt_identity
from controllers.user_controller import UserController

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users/register', methods=['POST'])
@jwt_required(optional=True)  # Vérifie la présence du jeton sans bloquer la route
def register():
    if get_jwt_identity():
        return redirect(url_for('main.index'))  # Redirige vers la route racine ("/")
    user_data = request.json
    return UserController.register_user(user_data)

@user_blueprint.route('/users/login', methods=['POST'])
@jwt_required(optional=True)  # Vérifie la présence du jeton sans bloquer la route
def login():
    if get_jwt_identity():
        return redirect(url_for('main.index'))  # Redirige vers la route racine ("/")
    return UserController.login_user()

@user_blueprint.route('/users/logout', methods=['GET'])
@jwt_required()
def logout():
    return UserController.logout_user()

@user_blueprint.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    return UserController.get_users()

@user_blueprint.route('/users/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    return UserController.get_user(user_id)

@user_blueprint.route('/users/edit/<int:user_id>', methods=['PUT'])
@jwt_required()
def edit_user(user_id):
    updated_data = request.json
    return UserController.edit_user(user_id, updated_data)

@user_blueprint.route('/users/delete/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    return UserController.delete_user(user_id)
