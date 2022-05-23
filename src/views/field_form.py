from flask import Blueprint

bp = Blueprint('field', __name__, url_prefix='/v1/form/field/')


@bp.route('/create/<form_uid>', methods=['POST'])
def create_field_form(form_uid):
    pass
# @bp.route('/update/<form_uid>', methods=['POST'])
# def update_field_form(form_uid):
#
# @bp.route('/delete/<form_uid>', methods=['POST'])
# def delete_field_form(form_uid):
