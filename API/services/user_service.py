# services/user_service.py
import json
import os
from models.user_model import User
from flask_jwt_extended import create_access_token

class UserService:

    @staticmethod
    def create_user(user_data):
        users = UserService.get_users()
        if any(user['email'] == user_data['email'] for user in users):
            return None
        new_user = User(id=len(users) + 1, **user_data)
        users.append(new_user.__dict__)
        UserService._save_users(users)
        return new_user.__dict__

    @staticmethod
    def login_user(user_id):
        # Créez un jeton JWT avec l'identifiant de l'utilisateur comme payload (identity)
        access_token = create_access_token(identity=user_id)
        return access_token
    
    @staticmethod
    def logout_user(response):
        try:
            response.delete_cookie('access_token')
        except Exception as e:
            raise Exception("Erreur lors de la déconnexion. Veuillez réessayer plus tard.")

    @staticmethod
    def get_users():
        file_path = "database/users.json"
        users = []
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                users = json.load(file)
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
            users.remove(user)
            UserService._save_users(users)
        return user

    @staticmethod
    def _save_users(users):
        file_path = "database/users.json"
        with open(file_path, "w") as file:
            json.dump(users, file, indent=2)

    @staticmethod
    def get_user_by_credentials(email, password):
        users = UserService.get_users()
        return next((user for user in users if user['email'] == email and user['password'] == password), None)
