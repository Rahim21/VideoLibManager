from flask import Flask, render_template, request , make_response
import requests

from routes.rule_route import rule_blueprint
from routes.page_route import page_blueprint
from routes.auth_route import auth_blueprint

app = Flask(__name__)

app.register_blueprint(rule_blueprint)
app.register_blueprint(page_blueprint)
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
