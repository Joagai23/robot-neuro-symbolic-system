from flask import Flask
from flask_cors import CORS
from waitress import serve
from src.api.api import api_bp

app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(api_bp, url_prefix='/api')

if __name__ == "__main__":
    serve(app, host="127.0.0.1", port=8080)