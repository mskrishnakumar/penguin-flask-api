from flask import Flask, request, jsonify
import requests
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("AZURE_ML_ENDPOINT")
DEPLOYMENT = os.getenv("DEPLOYMENT_NAME", "blue")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {API_KEY}',
            'azureml-model-deployment': DEPLOYMENT
        }
        response = requests.post(ENDPOINT, headers=headers, json=request.json)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        return jsonify({'error': str(e)}), 500
