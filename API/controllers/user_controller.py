# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/user_controller.py
from flask import jsonify, request, make_response
from services.user_service import UserService

class UserController:

    @staticmethod
    def register_user(user_data):
        try:
            user = UserService.create_user(user_data)
            if user:
                return jsonify({"statusCode": 201, "user": user})
            else:
                return jsonify({"statusCode": 400, "error": "L'utilisateur existe déjà."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def login_user():
        try:
            data = request.get_json()
            user = UserService.get_user_by_credentials(data['email'], data['password'])
            if user:
                # Création d'un jeton JWT
                token = UserService.login_user(user['id'])
                if token:
                    return jsonify({"statusCode": 200, "token": token})
                else:
                    return jsonify({"statusCode": 500, "error": "Erreur interne lors de la création du jeton."})
            else:
                return jsonify({"statusCode": 400, "error": "Identifiants incorrects."})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def logout_user():
        try:
            response = UserService.logout_user(make_response())
            return jsonify({"statusCode": 200, "message": "Déconnexion réussie.", "response":response})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})
        
    @staticmethod
    def get_users():
        try:
            users = UserService.get_users()
            return jsonify({"statusCode": 200, "users": users})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def get_user(user_id):
        try:
            user = UserService.get_user_by_id(user_id)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})
   
    @staticmethod 
    def edit_user(user_id, updated_data):
        try:
            user = UserService.update_user(user_id, updated_data)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def delete_user(user_id):
        try:
            user = UserService.delete_user(user_id)
            if not user:
                return jsonify({"statusCode": 200, "user": None})
            return jsonify({"statusCode": 200, "user": user})
        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})