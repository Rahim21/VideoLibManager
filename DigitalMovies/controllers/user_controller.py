# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/user_controller.py
from flask import make_response
from controllers.requestAPI import RequestAPI

class UserController:

    api_url = "http://127.0.0.1:5001"
    user_url = api_url + "/users"

    @staticmethod
    def register_user(user_data, route_url, method): # ajouter champs src et dest pour savoir de quel template il vient et où il se dirige ? en cas d'erreur ou success pour le rediriger
        username, email, password = (user_data.form.get(field, '') for field in ['username', 'email', 'password'])
        url = "{}/{}".format(UserController.user_url, route_url.rsplit('.', 1)[-1])
        # Créer un dictionnaire avec les champs non vides
        data = {
            key: value for key, value in {
                "pseudo": username,
                "email": email,
                "password": password,
            }.items() if value
        }
        return RequestAPI.request_to_api(method, str(url), data, f'{username} registered successfully!', 'Registration failed!')

    @staticmethod
    def login_user(user_data, route_url, method):
        email, password = (user_data.form.get(field, '') for field in ['email', 'password'])
        url = "{}/{}".format(UserController.user_url, route_url.rsplit('.', 1)[-1])
        data = {
            key: value for key, value in {
                "email": email,
                "password": password,
            }.items() if value
        }
        return RequestAPI.request_to_api(method, str(url), data, f'{email} logged in successfully!', 'Login failed!')

    @staticmethod
    def logout_user(route_url, method):
        response = make_response("Cookie Removed")
        response.set_cookie('saved_name', expires=0)
        response.set_cookie('token', expires=0)
        response.headers['Location'] = '/'
        response.status_code = 302
        response_data = {
            'type_msg': 'success',
            'message': 'You are now logged out!'
        }
        return response
        
    @staticmethod
    def get_users(method):
        url = UserController.user_url
        return RequestAPI.request_to_api(method, url, success_message='Users fetched successfully!', error_message='Failed to fetch users!')

    @staticmethod
    def get_user(user_id, route_url, method):
        url = "{}/{}".format(UserController.user_url, user_id)
        return RequestAPI.request_to_api(method, url, success_message=f'User {user_id} fetched successfully!', error_message=f'Failed to fetch user {user_id}!')

    @staticmethod 
    def edit_user(user_id, user_data, route_url, method):
        email, password, nom, prenom, pseudo, age, is_active = (
            user_data.form.get(field, '') for field in ['email', 'password', 'nom', 'prenom', 'pseudo', 'age', 'is_active']
        )
        # Dictionnaire avec les champs non vides
        data = {
            key: value for key, value in {
                "email": email,
                "password": password,
                "nom": nom,
                "prenom": prenom,
                "pseudo": "pseudo",
                "age": age,
                "is_active": is_active
            }.items() if value
        }
        url = "{}/{}".format(UserController.user_url, route_url.rsplit('.', 1)[-1])
        return RequestAPI.request_to_api(method, url, data, f'User {user_id} updated successfully!', f'Failed to update user {user_id}!')

    @staticmethod
    def delete_user(route_url, method):
        url = "{}/{}".format(UserController.user_url, route_url)
        return RequestAPI.request_to_api(method, url, success_message=f'User deleted successfully!', error_message=f'Failed to delete user!')