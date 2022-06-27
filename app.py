# app.py
import json
from os import abort
from flask import Flask, request, jsonify
from flask_api import status
from flask_sqlalchemy import SQLAlchemy

from employee import Employee, EmployeeEncoder

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://vhiwzwzghswasj:9f6b076dc51df117692a5275296f097efd749ff8c9f7cd3f5b0161f30b69e34c@ec2-34-198-186-145.compute-1.amazonaws.com:5432/d952ko673snplk'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)


@app.route('/login', methods=['POST'])
def login():
    body = request.json
    username = body.get('username')
    password = body.get('password')
    print(f'{username} - {password}')
    if (username == 'hoang7020' and password == '123456'):
        return jsonify(message='Login Success!!!', username=username, type=0), status.HTTP_200_OK
    if (username == 'boss1' and password == '123456'):
        return jsonify(message='Login Success!!!', username=username, type=1), status.HTTP_200_OK
    if (username == 'boss2' and password == '123456'):
        return jsonify(message='Login Success!!!', username=username, type=2), status.HTTP_200_OK
    return jsonify(message='Login Fail!!!'), status.HTTP_203_NON_AUTHORITATIVE_INFORMATION


@app.route('/submit', methods=['POSfT'])
def submit():
    body = request.json
    recevier = body.get('receiver')
    min_api_version = body.get('min_api_version')
    sender = body.get('sender')
    tracking_data = body.get('tracking_data')
    type = body.get('type')
    text = body.get('text')
    print(text)
    return "This application is summited"


@app.route('/load_all_applications', methods=['GET'])
def load_all_applications():
    return "all application"


@app.route('/load_most_unschedule_list', methods=['GET'])
def load_most_unschedule_list():
    employees = []
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("pham", 5, 3, "pham@rakute.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("minh", 3, 4, "minh@rakute.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("hoang", 2, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    employees.append(json.loads(EmployeeEncoder().encode(
        Employee("demo", 1, 1, "hoang@rakuten.com"))))
    return jsonify(employees=employees)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    db.create_all()
    app.run(threaded=True, port=5000)
