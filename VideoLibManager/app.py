from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def process_form():
    username = request.form['username']
    password = request.form['password']
    # Ajoutez ici le traitement du formulaire selon vos besoins
    return render_template('index.html', message=f'Form submitted by {username}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
