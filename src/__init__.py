import click
from flask import Flask
from flask.cli import with_appcontext
from flask_jsonrpc import JSONRPC
from flask_sqlalchemy import SQLAlchemy

from .config import DATABASE_URI
from .views import form

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    jsonrpc = JSONRPC(app, "/api", enable_web_browsable_api=True)

    app.config.from_mapping(
        # default secret that should be overridden in environ or config
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db.init_app(app)

    app.cli.add_command(init_db_command)

    app.register_blueprint(form.bp)
    # app.register_blueprint(docs.bp)
    # jsonrpc.register_blueprint(app, user, url_prefix='/user', enable_web_browsable_api=True)

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
