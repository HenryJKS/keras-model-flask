from flask import Flask
from app.routes.predict_route import predict_route
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    # Registrar o Blueprint de predição
    app.register_blueprint(predict_route)

    return app
