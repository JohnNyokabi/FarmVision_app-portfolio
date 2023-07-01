from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app, origins='http://localhost:8080', methods=['GET', 'POST'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'mysql://username:password@localhost/farmvision_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


# Farmer model
class Farmer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True, nullable=False)
    country = db.Column(db.String(50), nullable=False)
    identification = db.Column(db.String(50), nullable=False)
    farm_name = db.Column(db.String(100), nullable=False)
    farm_location = db.Column(db.String(50), nullable=False)
    farm_address = db.Column(db.Text, nullable=False)
    farming_type = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


@app.route('/farmers', methods=['POST'])
def create_farmer():
    data = request.json
    user_email = data.get('email')

    # Check if the user exists
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    country = data.get('country')
    identification = data.get('identification')
    farm_name = data.get('farm_name')
    if farm_name is None:
        return jsonify({'message': 'Farm name is required'}), 400
    farm_location = data.get('farm_location')
    
    farm_address = data.get('farm_address')

    farming_type = data.get('farming_type')
    """{
        'livestock': False,
        'crops': False
    }
    livestock_options = {}
    crop_options = {}

    # Retrieve selected options from the request payload
    selected_livestock = data.get('farmingType', {}).get('livestock')
    selected_crops = data.get('farmingType', {}).get('crops')

    # Set the appropriate values based on checkbox selection
    if selected_livestock:
        farming_type['livestock'] = True
        livestock_options = data.get('livestockOptions', {})

    if selected_crops:
        farming_type['crops'] = True
        crop_options = data.get('cropOptions', {})"""

    farmer = Farmer(
        user_id=user.id,
        country=country,
        identification=identification,
        farm_name=farm_name,
        farm_location = farm_location,
        farm_address=farm_address,
        farming_type=farming_type
    )
    db.session.add(farmer)
    db.session.commit()

    return jsonify({'message': 'Farmer created successfully'}), 201


@app.route('/farmers/<int:farmer_id>', methods=['GET'])
def get_farmer(farmer_id):
    farmer = Farmer.query.get(farmer_id)
    if not farmer:
        return jsonify({'message': 'Farmer not found'}), 404

    farmer_data = {
        'id': farmer.id,
        'userId': farmer.user_id,
        'country': farmer.country,
        'identification': farmer.identification,
        'farmName': farmer.farm_name,
        'farmLocation': farmer.farm_location,
        'farmAddress': farmer.farm_address,
        'farmingType': farmer.farm_type,
        'createdAt': farmer.created_at,
        'updatedAt': farmer.updated_at
    }

    return jsonify(farmer_data), 200


@app.route('/farmers/<int:farmer_id>', methods=['PUT'])
def update_farmer(farmer_id):
    farmer = Farmer.query.get(farmer_id)
    if not farmer:
        return jsonify({'message': 'Farmer not found'}), 404

    data = request.json
    country = data.get('country')
    identification = data.get('identification')
    farm_name = data.get('farm_name')
    farm_location = data.get('farm_location')
    farm_address = data.get('farmAddress')
    farming_type = data.get('farmingType')

    farmer.country = country
    farmer.identification = identification
    farmer.farm_name = farm_name
    farmer.farm_location = farm_location
    farmer.farm_address = farm_address
    farmer.farming_type = farming_type

    db.session.commit()

    return jsonify({'message': 'Farmer updated successfully'}), 200


@app.route('/farmers/<int:farmer_id>', methods=['DELETE'])
def delete_farmer(farmer_id):
    farmer = Farmer.query.get(farmer_id)
    if not farmer:
        return jsonify({'message': 'Farmer not found'}), 404

    db.session.delete(farmer)
    db.session.commit()

    return jsonify({'message': 'Farmer deleted successfully'}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5001, debug=True)
