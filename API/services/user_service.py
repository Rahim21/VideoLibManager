# services/user_service.py
import json
import os
from models.user_model import User

class UserService:
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
    def create_user(user_data):
        users = UserService.get_users()
        user = User(**user_data)
        users.append(user.__dict__)
        UserService._save_users(users)
        return user.__dict__

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
