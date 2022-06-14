# import the main blue print instance
from app.main import main
from flask import request, jsonify, abort
from flask import current_app
import logging


@main.route('/hello', methods=['GET'])
def hello():
    return 'Hello World'