from flask import Blueprint, render_template, request, url_for, redirect

from src.services.field_service import get_fields_form_or_none_template
from src.services.form_services import (validate_form_data,
                                        update_validated_form_or_none,
                                        delete_form_service,
                                        get_form_or_none)
from src.services.general_service import save_validate_instance_or_error

bp = Blueprint('form', __name__, url_prefix='/v1/form')


@bp.route('/', methods=['GET'])
@bp.route('/<form_uid>', methods=['GET'])
def get_form(form_uid=None):
    """
    Получение template для создания или изменения Form-ы.
    Если в параметрах указать form_uid существующей Form, то ее шаблон выведется пользователю.

    :return:
    """
    fields_form = None
    error = request.args.get('error')
    response = request.args.get('response')

    form = get_form_or_none(form_uid=form_uid)

    if form:
        fields_form = get_fields_form_or_none_template(form_id=form.id)

    return render_template('create_form/create_form.html', form=form, error=error, response=response,
                           fields_form=fields_form)


@bp.route('/update/<form_uid>', methods=['POST'])
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

    return redirect(url_for('form.get_form', error=error, form_uid=form.form_uid))


@bp.route('/delete/<form_uid>', methods=['POST'])
def delete_form(form_uid):
    """
    Обновление Form-ы.

    :return:
    """
    response = f'Вы удалили форму с form_uid: {form_uid}'

    id_form_deleted = delete_form_service(form_uid=form_uid)

    if id_form_deleted == 0:
        response = 'Такой формы уже/ещё нет'

    return redirect(url_for('form.get_form', response=response))


@bp.route('/', methods=['POST'])
def post_form():
    """
    Создание новой Form-ы
    :return:
    """
    save_error = 'Вы ввели не уникальный uid'

    validated_form = validate_form_data(request=request)
    form, error = save_validate_instance_or_error(validate_instance=validated_form, save_error=save_error)
    print(form)
    return render_template('create_form/create_form.html', form=form, error=error)
