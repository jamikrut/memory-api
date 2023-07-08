from flask import jsonify

from memoryapp import app
from memoryapp.exceptions import NotFoundException


@app.errorhandler(NotFoundException)
def handle_not_found(e: NotFoundException):
    return jsonify({'message': f'{e.item} not found'}), 404
