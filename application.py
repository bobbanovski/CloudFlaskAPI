from flask import flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    app.config.from_pyfile('settings.py')

    #apply overrides
    app.config.update(config_overrides)

    db.init_app(app)

    from home.views import home_app

    #register blueprints
    app.register_blueprint(home_app)

    return app