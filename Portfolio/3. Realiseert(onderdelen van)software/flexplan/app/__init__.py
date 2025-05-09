from flask import Flask

def create_app():
    app = Flask(__name__)
    from .routes.verlof import verlof_bp
    app.register_blueprint(verlof_bp)
    return app
