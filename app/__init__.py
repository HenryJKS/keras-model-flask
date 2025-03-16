from flask import Flask
from app.routes.predict_route import predict_route


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Registrar o Blueprint de predição
    app.register_blueprint(predict_route)

    return app
