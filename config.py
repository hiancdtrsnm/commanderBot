import os, json
ORDERS = os.getenv('ORDERS', 'ordersexample.json')
BATTLES = os.getenv('BATTLES', 'battles.json')
battles = json.load(open(BATTLES))