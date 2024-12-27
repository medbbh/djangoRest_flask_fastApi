from flask import Flask, request
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

EXTERNAL_API_BASE_URL = 'http://127.0.0.1:8000/api'

class ExternalItemList(Resource):
    def get(self):
        response = requests.get(f'{EXTERNAL_API_BASE_URL}/items/')
        return response.json() if response.status_code == 200 else (
            {"error": "Error fetching items"}, response.status_code
        )
        
    def post(self):
        item = request.get_json()
        if not item:
            return {"error": "No data provided"}, 400
            
        response = requests.post(f'{EXTERNAL_API_BASE_URL}/items/', json=item)
        return response.json() if response.status_code == 201 else (
            {"error": "Error posting item"}, response.status_code
        )

class ExternalItem(Resource):
    def get(self, id):
        response = requests.get(f'{EXTERNAL_API_BASE_URL}/items/{id}')
        return response.json() if response.status_code == 200 else (
            {"error": "Item not found"}, response.status_code
        )

    def delete(self, id):
        response = requests.delete(f'{EXTERNAL_API_BASE_URL}/items/{id}/')
        return response.json() if response.status_code == 200 else (
            {"error": "Error deleting item"}, response.status_code
        )

    def put(self, id):
        data = request.get_json()
        if not data:
            return {'error': 'No data provided'}, 400
            
        if 'name' not in data or 'description' not in data:
            return {'error': 'Name and description are required'}, 400
            
        response = requests.put(f'{EXTERNAL_API_BASE_URL}/items/{id}/', json=data)
        return response.json() if response.status_code == 200 else (
            {"error": "Error updating item"}, response.status_code
        )

api.add_resource(ExternalItemList, '/items')
api.add_resource(ExternalItem, '/items/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)