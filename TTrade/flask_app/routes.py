from flask import jsonify, abort, request
from flask_app import app
from app import Account
from app.util import get_price

@app.errorhandler(404)
def error404():
    return jsonify({'error': '404 not found'}), 404

@app.errorhandler(500)
def error500():
    return jsonify({'error': 'application error'}), 500

@app.route('/api/<api_key>/balance', methods=['GET'])
def balance(api_key):
    account = Account.authenticate_api(api_key)
    if not account:
        return jsonify({"error": "authentication error"}), 400
    return jsonify({"username": account.username, "balance": account.balance})


@app.route('/api/price/<ticker>', methods=['GET'])
def lookup(ticker):
    ticker = get_price(ticker)
    if not ticker:
        return jsonify({'invalid': 'ticker'}), 404
    return jsonify({'price': ticker})

# @app.route('api/<api_key>/positions', methods=['GET'])
# def positions(api_key, ticker):
#     return ""

# @app.route('/api/<api_key>/position/<ticker>', methods=['GET'])
# def trades(api_key, ticker):
#     return ""

# @app.route('/api/<api_key>/alltrades', methods=['GET'])
# def all_trades(api_key, ticker):
#     return ""

# @app.route('api/<api_key>/buy', methods=['POST'])
# def buy(api_key):
#     return ""

# @app.route('api/<api_key>/sell', methods=['POST'])
# def sell(api_key):
#     return ""

@app.route('/api/<api_key>/deposit', methods=['PUT'])
def deposit(api_key):
    account = Account.authenticate_api(api_key)
    if not account:
        jsonify({'error': 'authentication error'}), 401
    if not request.json:
        return jsonify({'error': 'bad request'}), 400
    try:
        amount = request.json['amount']
        if amount < 0.0:
            raise ValueError
        account.balance += amount
    except(ValueError,KeyError):
        return jsonify({'error': 'bad request'}), 400
    account.save()
    return jsonify({'username': account.username, 'balance': account.balance})