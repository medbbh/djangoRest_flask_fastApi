from flask import Flask, request
from flask_restx import Api, Resource, fields
import requests

app = Flask(__name__)
api = Api(
    app,
    version='1.0',
    title='Items API',
    description='A simple Items API Gateway',
    doc='/docs'
)

# Define namespaces
ns = api.namespace('items', description='Items operations')

# Define models for request/response documentation
item_model = api.model('Item', {
    'id': fields.Integer(readonly=True, description='The item identifier'),
    'name': fields.String(required=True, description='The item name'),
    'description': fields.String(required=True, description='The item description')
})

item_input_model = api.model('ItemInput', {
    'name': fields.String(required=True, description='The item name'),
    'description': fields.String(required=True, description='The item description')
})

error_model = api.model('Error', {
    'error': fields.String(description='Error message')
})

EXTERNAL_API_BASE_URL = 'http://127.0.0.1:8000/api'

@ns.route('')
class ExternalItemList(Resource):
    @ns.doc('list_items')
    @ns.response(200, 'Success', [item_model])
    @ns.response(500, 'Server Error', error_model)
    def get(self):
        """List all items"""
        response = requests.get(f'{EXTERNAL_API_BASE_URL}/items/')
        return response.json() if response.status_code == 200 else (
            {"error": "Error fetching items"}, response.status_code
        )
    
    @ns.doc('create_item')
    @ns.expect(item_input_model)
    @ns.response(201, 'Item created', item_model)
    @ns.response(400, 'Validation Error', error_model)
    @ns.response(500, 'Server Error', error_model)
    def post(self):
        """Create a new item"""
        item = request.get_json()
        if not item:
            return {"error": "No data provided"}, 400
            
        response = requests.post(f'{EXTERNAL_API_BASE_URL}/items/', json=item)
        return response.json() if response.status_code == 201 else (
            {"error": "Error posting item"}, response.status_code
        )

@ns.route('/<int:id>')
@ns.param('id', 'The item identifier')
@ns.response(404, 'Item not found', error_model)
class ExternalItem(Resource):
    @ns.doc('get_item')
    @ns.response(200, 'Success', item_model)
    def get(self, id):
        """Fetch an item by ID"""
        response = requests.get(f'{EXTERNAL_API_BASE_URL}/items/{id}')
        return response.json() if response.status_code == 200 else (
            {"error": "Item not found"}, response.status_code
        )

    @ns.doc('delete_item')
    @ns.response(200, 'Item deleted')
    def delete(self, id):
        """Delete an item"""
        response = requests.delete(f'{EXTERNAL_API_BASE_URL}/items/{id}')
        return response.json() if response.status_code == 200 else (
            {"error": "Error deleting item"}, response.status_code
        )

    @ns.doc('update_item')
    @ns.expect(item_input_model)
    @ns.response(200, 'Success', item_model)
    @ns.response(400, 'Validation Error', error_model)
    def put(self, id):
        """Update an item"""
        data = request.get_json()
        if not data:
            return {'error': 'No data provided'}, 400
            
        if 'name' not in data or 'description' not in data:
            return {'error': 'Name and description are required'}, 400
            
        response = requests.put(f'{EXTERNAL_API_BASE_URL}/items/{id}', json=data)
        return response.json() if response.status_code == 200 else (
            {"error": "Error updating item"}, response.status_code
        )

if __name__ == '__main__':
    app.run(debug=True, port=5000)