from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, create_access_token
from models import db, Product, Client

routes = Blueprint('routes', __name__)

@routes.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')  # Altere para o campo correto
    password = request.json.get('password')  # Altere para o campo correto
    # Adicione a verificação de usuário aqui
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@routes.route('/products', methods=['GET'])
@jwt_required()
def get_products():
    products = Product.query.all()
    return jsonify([p.serialize() for p in products])

@routes.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.get_json()
    new_product = Product(name=data['name'], price=data['price'], stock=data['stock'])
    db.session.add(new_product)
    db.session.commit()
    return jsonify(message="Product added"), 201

@routes.route('/clients', methods=['GET'])
@jwt_required()
def get_clients():
    clients = Client.query.all()
    return jsonify([c.serialize() for c in clients])

@routes.route('/clients', methods=['POST'])
@jwt_required()
def add_client():
    data = request.get_json()
    new_client = Client(name=data['name'], email=data['email'], phone=data.get('phone'))
    db.session.add(new_client)
    db.session.commit()
    return jsonify(message="Client added"), 201
