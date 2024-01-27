from flask import Flask, render_template, request , make_response
import requests

from routes.rule_route import rule_blueprint
from routes.page_route import page_blueprint
from routes.user_route import user_blueprint
from routes.movie_route import movie_blueprint

app = Flask(__name__)
app.secret_key = 'ProjetFlaskDigitalMovies'

app.register_blueprint(rule_blueprint)  # règle de l'app
app.register_blueprint(page_blueprint) # page web
app.register_blueprint(user_blueprint, url_prefix='/users') # requete API users
app.register_blueprint(movie_blueprint, url_prefix='/movies') # requete API movies

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
