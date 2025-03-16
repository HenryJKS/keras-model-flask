from flask import Flask, render_template, session, url_for
import numpy as np
from wtforms import FlaskForm
from keras.api.models import load_model
import joblib

model = load_model('tensorflow_model/final_model_iris.keras')
iris_scaler = joblib.load('tensorflow_model/scaler/iris_scaler.pkl')

# 'setosa', 'versicolor', 'virginica'
def model_predict(flower_json):
    class_labels = np.array(["setosa", "versicolor", "virginica"])

    np_features = np.array(
        [flower_json['sepal_length'], flower_json['sepal_width'], flower_json['petal_length'], flower_json['petal_width']])

    np_features_scaler = iris_scaler.transform([np_features])

    pred = model.predict(np_features_scaler, verbose=0)

    prediction = np.argmax(pred, axis=1)[0]

    return {'Prediction': class_labels[prediction], 'Confidence': float(np.max(pred))}

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    content = request.json
    results = model_predict(content)
    return jsonify(results)

@app.route('/')
def home():
    return "<h1>Hello, World!</h1>"

if __name__ == '__main__':
    app.run()