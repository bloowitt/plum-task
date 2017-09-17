# -*- coding: utf-8 -*-

from werkzeug.exceptions import BadRequest
from flask import Blueprint, current_app, jsonify, request
from utils import get_request_params_for_search

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


@api.route('/search', methods=['GET'])
def search():
    # Param sanity checks and handling should be done with something like Cerberus
    try:
        params = get_request_params_for_search(request.args)
    except Exception as e:
        raise BadRequest(e)
    products = current_app.data.get_filtered_products(params['lat'], 
                                                        params['lng'], 
                                                        params['radius'], 
                                                        params['tags'])         
    return jsonify({'products': [product.serialize() for product in products[0:params['count']]]})
