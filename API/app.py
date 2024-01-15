# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# app.py
import os
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from routes.user_route import user_blueprint
from routes.movie_route import movie_blueprint

app = Flask(__name__)
app.secret_key = 'ProjetFlask'

# Configurer paramètres de JWT
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'VideoLibManager')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400  # expire après 24 heures
jwt = JWTManager(app)
CORS(app)

app.register_blueprint(user_blueprint)

@app.route('/')
def hello_world():
    return 'API : VideoLib Manager'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
