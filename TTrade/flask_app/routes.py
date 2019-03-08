from flask import jsonify, abort, request
from flask_app import app
from app import Account, Trade
from app.util import get_price
# from app.position import positions_json
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

@app.route('/api/<api_key>/positions', methods=['GET'])
def positions(api_key):
    account = Account.authenticate_api(api_key)
    if not account:
        return jsonify({'error': 'authentication error'}), 400
    position = account.get_positions_json()
    return jsonify({'positions': position})


@app.route('/api/price/<ticker>', methods=['GET'])
def lookup(ticker):
    ticker = get_price(ticker)
    if not ticker:
        return jsonify({'invalid': 'ticker'}), 404
    return jsonify({'price': ticker})

@app.route('/api/<api_key>/positions/<ticker>', methods=['GET'])
def trades(api_key, ticker):
    account = Account.authenticate_api(api_key)
    if not account:
        return jsonify({'invalid': ticker}), 404
    position = account.get_position_for_json(ticker)
    return jsonify({'position': position})

@app.route('/api/<api_key>/alltrades', methods=['GET'])
def all_trades(api_key):
    account = Account.authenticate_api(api_key)
    if not account:
        return jsonify({'error': 'authentication error'}), 404
    trades = account.get_trades_json()
    return jsonify({'trades': trades})


# @app.route('/api/<api_key>/buy/<ticker>/<int:amount>', methods=['POST'])
# def buy(api_key, ticker, amount):
#     account = Account.authenticate_api(api_key)
#     if not account:
#         return jsonify({'error': 'authentication error'}), 401
#     if not request.json:
#         return jsonify({'error': 'bad request'})
#     ticker = get_price(ticker)
#     price = ticker[1]
#     total_cost = int(amount) *int(price)
#     trade = Account.buy(account, ticker, amount, price, total_cost)


# @app.route('api/<api_key>/sell', methods=['POST'])
# def sell(api_key):
#     return ""

@app.route('/api/<api_key>/deposit', methods=['PUT'])
def deposit(api_key):
    account = Account.authenticate_api(api_key)
    if not account:
        return jsonify({'error': 'authentication error'}), 401
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