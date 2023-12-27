# controllers/user_controller.py
from flask import jsonify, request
from services.user_service import UserService

class UserController:

    @staticmethod
    def register_user(user_data):
        try:
            # Appelle le service d'inscription
            user = UserService.create_user(user_data)

            # Retourne la réponse appropriée
            if user:
                return jsonify({"statusCode": 201, "user": user})
            else:
                return jsonify({"statusCode": 400, "error": "L'utilisateur existe déjà."})

        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def login():
        try:
            # Récupère les données d'authentification depuis la requête
            email = request.json.get('email')
            password = request.json.get('password')

            # Appelle le service d'authentification
            token = UserService.login_user(email, password)

            # Retourne la réponse appropriée
            if token:
                return jsonify({"statusCode": 200, "token": token})
            else:
                return jsonify({"statusCode": 400, "error": "Identifiants incorrects."})

        except Exception as e:
            return jsonify({"statusCode": 500, "error": "Erreur interne. Veuillez réessayer plus tard."})

    @staticmethod
    def logout():
        try:
            # Appelle le service de déconnexion
            UserService.logout_user()

            # Retourne la réponse appropriée
            return jsonify({"statusCode": 200, "message": "Déconnexion réussie."})

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