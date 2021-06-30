# app.py
# Purpose: Create a Flask app and define the necessary API routes

from flask import Flask, render_template, request, jsonify
import db
from flask import jsonify
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('home.html')


@app.route('/api/v1/todo', methods=['POST'])
@auth.login_required
def create_todo():
    request_data = request.get_json()
    new_todo = {
        'id': request_data['id'],
        'name': request_data['name'],
        'company': request_data['company']
    }
    db.insert_into(new_todo)
    return jsonify(new_todo)


@app.route('/api/v1/todos')
@auth.login_required
def get_response():
    return jsonify({'todos': db.get_all()})


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'user' and password == 'password':
            return True
        else:
            return False
    return False





# Running on port number
app.run(port=9696)