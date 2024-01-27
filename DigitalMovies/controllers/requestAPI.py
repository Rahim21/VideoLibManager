# -----------------------------------------------------------------------------
# Auteurs: HAYAT Rahim et DRIOUCHE Sami
# -----------------------------------------------------------------------------
# controllers/requestAPI.py
from flask import jsonify, request
import requests

class RequestAPI:

    def request_to_api(method, url, data=None, success_message='Received!', error_message='Failed!'):
        headers = {'Content-Type': 'application/json'}
        token = request.cookies.get('token')
        if token:
            headers.update({'Authorization': f'Bearer {token}'})
        response = requests.request(method, url, json=data, headers=headers)
        if response.json().get('statusCode', '') in [200, 201]:
            return jsonify({
                'data': response.json(),
                'type_msg': 'success',
                'message': success_message
            })
        else:
            return jsonify({
                'data': data,
                'type_msg': 'error',
                'message': error_message
            })