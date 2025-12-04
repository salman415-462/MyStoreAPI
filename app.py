from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Your data
data = {
  "products": [
    {"id": 1, "name": "iPhone 15", "price": 999, "category": "electronics"},
    {"id": 2, "name": "MacBook Pro", "price": 1999, "category": "electronics"}
  ],
  "users": [
    {"id": 1, "username": "john_doe", "email": "john@example.com"}
  ]
}

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(data['products'])

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data['users'])

@app.route('/carts', methods=['GET'])
def get_carts():
    return jsonify([])

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify([])

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
