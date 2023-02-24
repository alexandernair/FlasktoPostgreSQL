from flask import jsonify
from app import app, db, Item


@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify({'items': [{'id': item.id, 'name': item.name} for item in items]})
