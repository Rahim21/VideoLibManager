# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# services/user_service.py
import json
import os
import uuid
from models.user_model import User
from flask import jsonify, make_response
from flask_jwt_extended import create_access_token, unset_jwt_cookies
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:

    @staticmethod
    def create_user(user_data):
        users = UserService.get_users()
        if users:
            if any(user['email'] == user_data['email'] for user in users):
                return None
        user_data['password'] = generate_password_hash(user_data['password'], method='pbkdf2:sha256')
        new_user = User(id=str(uuid.uuid4()), **user_data)
        users.append(new_user.__dict__)
        UserService._save_users(users)
        return new_user.__dict__

    @staticmethod
    def get_user_by_credentials(email, password):
        users = UserService.get_users()
        for user in users:
            try:
                if user['email'] == email and check_password_hash(user['password'], password):
                    return user
            except Exception as e:
                print(f"Error comparing passwords: {e}")
        return None

    @staticmethod
    def login_user(user_id):
        # Créez un jeton JWT avec l'identifiant de l'utilisateur comme payload (identity)
        access_token = create_access_token(identity=user_id)
        return access_token
    
    @staticmethod
    def logout_user(response):
        try:
            response = make_response(jsonify(msg="Déconnecté avec succès"), 200)
            unset_jwt_cookies(response)
            return response

        except Exception as e:
            raise Exception("Erreur lors de la déconnexion. Veuillez réessayer plus tard.")

    @staticmethod
    def get_users():
        file_path = "database/users.json"
        users = []
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path, "r") as file:
                users = json.load(file)
        else:
            with open(file_path, "w") as file:
                json.dump([], file)
        return users

    @staticmethod
    def get_user_by_id(user_id):
        users = UserService.get_users()
        user = next((u for u in users if u['id'] == user_id), None)
        return user

    @staticmethod
    def update_user(user_id, updated_data):
        users = UserService.get_users()
        user = next((u for u in users if u['id'] == user_id), None)
        if user:
            user.update(updated_data)
            UserService._save_users(users)
        return user

    @staticmethod
    def delete_user(user_id):
        users = UserService.get_users()
        user = next((u for u in users if u['id'] == user_id), None)
        if user:
            # users.remove(user)
            user['is_active'] = False
            UserService._save_users(users)
        return user

    @staticmethod
    def _save_users(users):
        file_path = "database/users.json"
        with open(file_path, "w") as file:
            json.dump(users, file, indent=2)
