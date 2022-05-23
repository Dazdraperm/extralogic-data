from flask import Blueprint, render_template, request, url_for, Response

from src.models import Form
from src.services.form_services import validate_form_data, insert_validated_instance_or_none, \
    update_validated_form_or_none

bp = Blueprint('form', __name__, url_prefix='/v1/form')


@bp.route('/', methods=['GET'])
@bp.route('/<form_uid>', methods=['GET'])
def get_form(form_uid=None):
    """
    Получение template для создания или изменения Form-ы.
    Если в параметрах указать form_uid существующей Form, то ее шаблон выведется пользователю.

    :return:
    """
    error = request.args.get('error')

    form = Form.query.filter_by(form_uid=form_uid).first()

    return render_template('create_form.html', form=form, error=error)


@bp.route('/<form_uid>', methods=['PUT'])
def update_form(form_uid):
    """
    Обновление Form-ы.

    :return:
    """
    error = None
    form = None
    validated_form = validate_form_data(request=request)

    if validated_form:
        form = update_validated_form_or_none(validated_form, form_uid)
    else:
        error = 'Вы ввели не валидные данные'

    if (error is None) and (form is None):
        error = 'Вы ввели не уникальный uid'

    return render_template('create_form.html', form=form, error=error)


@bp.route('/<form_uid>', methods=['DELETE'])
def delete_form():
    """
    Обновление Form-ы.

    :return:
    """

    return url_for()


@bp.route('/', methods=['POST'])
def post_form():
    """
    Создание новой Form-ы
    :return:
    """
    error = None
    form = None
    validated_form = validate_form_data(request=request)

    if validated_form:
        form = insert_validated_instance_or_none(validated_form)
    else:
        error = 'Вы ввели не валидные данные'

    if (error is None) and (form is None):
        error = 'Вы ввели не уникальный uid'

    return render_template('create_form.html', form=form, error=error)
