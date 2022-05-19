from flask import Flask
from flask_jsonrpc import JSONRPC


def create_app():
    app = Flask(__name__)
    jsonrpc = JSONRPC(app, "/api", enable_web_browsable_api=True)

    from .views import form

    app.register_blueprint(form.bp)
    # app.register_blueprint(docs.bp)
    # jsonrpc.register_blueprint(app, user, url_prefix='/user', enable_web_browsable_api=True)

    return app
