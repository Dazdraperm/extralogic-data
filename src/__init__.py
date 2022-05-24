import click
from flask import Flask
from flask.cli import with_appcontext
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy

from .config import DevConfig


db = SQLAlchemy()
jsonrpc = JSONRPC()


def create_app():
    """Create and config app"""

    app = Flask(__name__)

    # Give config from object
    app.config.from_object(DevConfig)

    # JsonRPC and DB instance
    jsonrpc.init_app(app)
    db.init_app(app)

    # For command "flask init-db"
    app.cli.add_command(init_db_command)

    # Register blueprints
    from .views import form, field_form
    app.register_blueprint(form.bp)
    app.register_blueprint(field_form.bp)

    # Register json-rpc blueprints
    from .api import rpc_bp
    jsonrpc.register_blueprint(app, rpc_bp, url_prefix='/form', enable_web_browsable_api=True)

    return app


def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
