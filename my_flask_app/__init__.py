from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = '7040746d0b3d38ba7f704e9d2e5aac42'
    from . import app
    return app
