from flask import Blueprint, request, redirect, url_for, Response, render_template

from src.services.field_service import validate_field_data
from src.services.form_services import get_form_or_none
from src.services.general_service import save_validate_instance_or_error

bp = Blueprint('field', __name__, url_prefix='/v1/form/field/')


@bp.route('/create/<form_uid>', methods=['POST'])
def create_field_form(form_uid):
    save_error = 'Не удалось сохранить'

    # Проверяем, что существует Form с таким form_uid
    form = get_form_or_none(form_uid)
    if not form:
        return Response(response='Формы с таким form_uid не существует', status=500)

    validated_field = validate_field_data(request=request, form_id=form.id)
    form_field, error = save_validate_instance_or_error(validate_instance=validated_field, save_error=save_error)

    return redirect(url_for('form.get_form', form_uid=form_uid))


# @bp.route('/update/<form_uid>', methods=['POST'])
# def update_field_form(form_uid):
#
# @bp.route('/delete/<form_uid>', methods=['POST'])
# def delete_field_form(form_uid):
