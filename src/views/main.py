from flask import Blueprint, render_template

bp = Blueprint('main', __name__, url_prefix='')

@bp.route('/', methods=['GET'])
def get_form():
    return render_template('main.html')