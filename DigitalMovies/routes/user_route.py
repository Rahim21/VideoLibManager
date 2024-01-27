# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# routes/user_route.py
from flask import Blueprint, request, render_template, make_response, redirect, url_for, session, g
import requests
from controllers.user_controller import UserController
from .rule_route import require_token

user_blueprint = Blueprint('user', __name__, url_prefix='/users')

@user_blueprint.route('/register', methods=['POST'])
def register():
    data = UserController.register_user(request, request.endpoint, request.method)
    return render_template('login.html', data=data)

@user_blueprint.route('/login', methods=['POST'])
def login():
    # return UserController.login_user(request, request.endpoint, request.method)
    response = UserController.login_user(request, request.endpoint, request.method)
    response_data = response.get_json()
    if response_data.get('type_msg') == 'success':  # If login was successful
        token = response_data.get('data').get('token', '')
        resp = make_response(redirect(url_for('page.index')))
        resp.set_cookie('token', token) # , httponly=False, secure=True
        # resp.headers['Location'] = '/'
        resp.status_code = 302
        session['data'] = response_data
        # Redirect to the index page
        return resp
    else:
        # If login failed, render the same login page with the response data
        return render_template('login.html', data=response_data)

@user_blueprint.route('/logout', methods=['GET'])
def logout():
    return UserController.logout_user(request.endpoint, request.method)

@user_blueprint.route('/', methods=['GET'])
def get_users():
    return UserController.get_users(request.method)

@user_blueprint.route('/<string:user_id>', methods=['GET'])
def get_user(user_id):
    return UserController.get_user(user_id, request.endpoint, request.method)

@user_blueprint.route('/<string:user_id>/edit', methods=['POST'])
@require_token
def edit_user(user_id):
    user_data = UserController.edit_user(user_id, request, f'{user_id}/edit', "PUT")
    #retourne la page de l'utilisateur modifié
    return render_template('profile.html', data=user_data , cookie=g.token) 

@user_blueprint.route('/<string:user_id>/delete', methods=['POST'])
@require_token
def delete_user(user_id):
    UserController.delete_user(f'{user_id}/delete', 'DELETE')
    users_data = UserController.get_users('GET')
    return render_template('dashboard.html', data=users_data , cookie=g.token) 
