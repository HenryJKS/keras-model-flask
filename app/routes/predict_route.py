from flask import Blueprint, jsonify, render_template, session, url_for, redirect, request
from app.forms.model_flower_classification import FlowerForm
from app.predictors.model_predict import model_flower_classification

predict_route = Blueprint('predict_route', __name__)

@predict_route.route('/api/predict', methods=['POST'])
def api_predict():
    try:
        content = request.json
        results = model_flower_classification(content)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)})

@predict_route.route('/predict', methods=['GET'])
def predict():
    if not session.get('sepal_length'):
        return redirect(url_for('predict_route.index'))

    content = {
        'sepal_length': float(session['sepal_length']),
        'sepal_width': float(session['sepal_width']),
        'petal_length': float(session['petal_length']),
        'petal_width': float(session['petal_width'])
    }

    results = model_flower_classification(content)

    return render_template('predict.html', results=results)


@predict_route.route('/', methods=['GET', 'POST'])
def index():
    form = FlowerForm()

    if form.validate_on_submit():
        session['sepal_length'] = form.sepal_length.data
        session['sepal_width'] = form.sepal_width.data
        session['petal_length'] = form.petal_length.data
        session['petal_width'] = form.petal_width.data

        return redirect(url_for("predict_route.predict"))
    return render_template("index.html", form=form)
