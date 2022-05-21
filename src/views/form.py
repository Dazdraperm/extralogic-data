from flask import Blueprint, render_template

from src.models import Form

bp = Blueprint('form', __name__, url_prefix='/form/v1')


@bp.route('/', methods=['GET'])
def get_form():
    return render_template('create_form.html')


@bp.route('/create', methods=['POST'])
def form_save():
    return {'a': 'Hello World!'}
