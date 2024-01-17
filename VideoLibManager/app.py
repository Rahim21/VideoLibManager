from flask import Flask, render_template, request , make_response
import requests

app = Flask(__name__)

@app.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/form_register', methods=['POST'])
def form_register():
    username, email, password = (request.form[field] for field in ['username', 'email', 'password'])
    
    url = "http://127.0.0.1:5001/users/register"
    data = {
        "pseudo": username,
        "email": email,
        "password": password,
    }
   
    response = requests.post(url, json=data) # POST
    # response = requests.get(url, headers={'Authorization': f'Bearer {token}'}) # GET

    if response.json().get('statusCode', '') == 200:
        return render_template('index.html', message=f'{username} registered successfully!')
    else:
        return render_template('index.html', message='Registration failed!')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/form_login', methods=['POST'])
def form_login():
    
    email, password = (request.form[field] for field in [ 'email', 'password'])
    url = "http://127.0.0.1:5001/users/login"
    data = {
        "email": email,
        "password": password,
    }
    response = requests.post(url, json=data)
    if response.json().get('statusCode', '') == 200:
        # Si la requête a réussi, récupérez le champ 'token' de la réponse JSON
        token = response.json().get('token', '')
        print("le token est : ,"+ token)
        resp = make_response(f"Cookie added !")
        resp.set_cookie('token', token) # , httponly=False, secure=True
       
        # return render_template('index.html', message=f'{email} logged in successfully! Token : {token}', cookie=resp)
        resp.headers['Location'] = '/'
        resp.status_code = 302
        return resp
    else:
        return render_template('index.html', message='Login failed!')

@app.route('/logout')
def logout():
    # Suppression du cookie contenant le token
    response = make_response("Cookie Removed")
    response.set_cookie('saved_name', expires=0)
    response.set_cookie('token', expires=0)
    response.headers['Location'] = '/'
    response.status_code = 302
    return response

@app.route('/')
def index():
    token = request.cookies.get('token')
    return render_template('index.html', cookie=token)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
