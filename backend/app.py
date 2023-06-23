#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from flask_cors import CORS
import secrets
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, origins='http://localhost:8080', methods=['GET', 'POST'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'mysql://username:password@localhost/farmvision_db')
app.config['SECRET_KEY'] = secrets.token_hex(16)
app.config['JWT_SECRET_KEY'] = secrets.token_hex(16)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Sign-up route
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')

    # Check if the email already exists
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({'message': 'Email already exists'}), 400

    # Hash the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user
    user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User created successfully'}), 201


# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid email or password'}), 401

    # Generate access token
    access_token = create_access_token(identity=user.id)

    return jsonify({'token': access_token, 'user': {'id': user.id, 'email': user.email, 'firstName': user.first_name, 'lastName': user.last_name}}), 200


# Forgot password route
@app.route('/forgot', methods=['POST'])
def forgot_password():
    data = request.json
    email = data.get('email')

    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Generate reset token
    token = serializer.dumps(user.id, salt='reset-password')

    # Send password reset email (implement your email sending logic here)

    return jsonify({'message': 'Password reset email sent'}), 200


# Reset password route
@app.route('/reset', methods=['POST'])
def reset_password():
    data = request.json
    password = data.get('password')
    confirm_password = data.get('confirmPassword')
    token = data.get('token')

    try:
        # Verify and load the token
        user_id = serializer.loads(token, salt='reset-password', max_age=3600)
    except SignatureExpired:
        return jsonify({'message': 'Reset token has expired'}), 400
    except Exception:
        return jsonify({'message': 'Invalid reset token'}), 400

    # Find the user by ID
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    # Update the password
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user.password = hashed_password
    db.session.commit()

    return jsonify({'message': 'Password reset successfully'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()

