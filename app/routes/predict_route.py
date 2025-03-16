from flask import Blueprint, request, jsonify
from app.predictors.model_predict import model_flower_classification

predict_route = Blueprint('predict_route', __name__)

@predict_route.route('/api/predict', methods=['POST'])
def predict():
    try:
        content = request.json
        results = model_flower_classification(content)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})
