from flask import Flask
from routes.user_route import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint)

@app.route('/')
def hello_world():
    return 'API : VideoLib Manager'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
