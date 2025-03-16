from keras.api.models import load_model
import joblib
import numpy as np

model = load_model('app/models/tensorflow_model/final_model_iris.keras')
iris_scaler = joblib.load('app/models/tensorflow_model/scaler/iris_scaler.pkl')

# 'setosa', 'versicolor', 'virginica'
def model_flower_classification(flower_json):
    class_labels = np.array(["setosa", "versicolor", "virginica"])

    np_features = np.array(
        [flower_json['sepal_length'], flower_json['sepal_width'], flower_json['petal_length'], flower_json['petal_width']])

    np_features_scaler = iris_scaler.transform([np_features])

    pred = model.predict(np_features_scaler, verbose=0)

    prediction = np.argmax(pred, axis=1)[0]

    return {'Prediction': class_labels[prediction], 'Confidence': float(np.max(pred))}