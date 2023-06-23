#!/usr/bin/python3
"""Creates the animal database"""

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from datetime import datetime
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure MySQL
CORS(app, origins='http://localhost:8080', methods=['GET', 'POST'])
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', 'mysql://username:password@localhost/farmvision_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create SQLAlchemy instance
db = SQLAlchemy(app)

# Define Animal model
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(100), nullable=False)
    breed = db.Column(db.String(100))
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(10), nullable=False)
    start_date = db.Column(db.Date)
    slaughter_date = db.Column(db.Date)
    date_served = db.Column(db.Date)
    production_system = db.Column(db.String(100), nullable=False)
    feed_type = db.Column(db.String(100))
    amount_administered = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'breed': self.breed,
            'dateOfBirth': str(self.date_of_birth),
            'gender': self.gender,
            'startDate': str(self.start_date),
            'slaughterDate': str(self.slaughter_date),
            'dateServed': str(self.date_served),
            'productionSystem': self.production_system,
            'feedType': self.feed_type,
            'amountAdministered': self.amount_administered
        }

# Create the Animal table in the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/api/animals', methods=['GET', 'OPTIONS'])
def get_animals():
    if request.method == 'OPTIONS':
        return ''
    animals = Animal.query.all()
    animals_data = [animal.to_dict() for animal in animals]
    return jsonify(animals_data)


@app.route('/api/animals', methods=['POST'])
def create_animal():
    data = request.get_json()
    try:
        start_date = datetime.strptime(data['startDate'], '%Y-%m-%d').date()
    except ValueError:
        return jsonify({'error': 'Invalid start date format. Expected format: YYYY-MM-DD'}), 400
    
    animal = Animal(
        name=data['name'],
        type=data['type'],
        breed=data['breed'],
        date_of_birth=data['dateOfBirth'],
        gender=data['gender'],
        start_date=start_date,
        slaughter_date=data['slaughterDate'],
        date_served=data['dateServed'],
        production_system=data['productionSystem'],
        feed_type=data['feedType'],
        amount_administered=data['amountAdministered']
    )
    db.session.add(animal)
    db.session.commit()
    return jsonify({'message': 'Animal created successfully'})

@app.route('/api/animals/<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    animal = Animal.query.get(animal_id)
    if animal:
        return jsonify(animal.to_dict())
    else:
        return jsonify({'message': 'Animal not found'}), 404

@app.route('/api/animals/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    animal = Animal.query.get(animal_id)
    if animal:
        data = request.get_json()
        animal.name = data.get('name', animal.name)
        animal.type = data.get('type', animal.type)
        animal.breed = data.get('breed', animal.breed)
        animal.date_of_birth = data.get('dateOfBirth', animal.date_of_birth)
        animal.gender = data.get('gender', animal.gender)
        animal.start_date = data.get('startDate', animal.start_date)
        animal.slaughter_date = data.get('slaughterDate', animal.slaughter_date)
        animal.date_served = data.get('dateServed', animal.date_served)
        animal.production_system = data.get('productionSystem', animal.production_system)
        animal.feed_type = data.get('feedType', animal.feed_type)
        animal.amount_administered = data.get('amountAdministered', animal.amount_administered)
        db.session.commit()
        return jsonify({'message': 'Animal updated successfully'})
    else:
        return jsonify({'message': 'Animal not found'}), 404

@app.route('/api/animals/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    animal = Animal.query.get(animal_id)
    if animal:
        db.session.delete(animal)
        db.session.commit()
        return jsonify({'message': 'Animal deleted successfully'})
    else:
        return jsonify({'message': 'Animal not found'}), 404

if __name__ == '__main__':
    app.run(port=5002)