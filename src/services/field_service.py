from typing import Optional

from flask import Request
from sqlalchemy.orm.exc import StaleDataError

from src import db
from src.models import TypeField, FieldForm, Form


def check_type_field_or_none(type_field: str) -> Optional[int]:
    """
    Возвращает id TypeField, по заданному type_field или None если такого не существует

    :param type_field: (select, textare, input, etc...)
    :return:
    """
    type_field = TypeField.query.filter_by(type_field=type_field).first()

    if type_field:
        return type_field.id
    else:
        return None


def validate_field_data(request: Request, form_id: int) -> Optional[FieldForm]:
    """
    Проверка данных поля (FieldForm) формы
    :param form_id: id Form
    :param request:
    :return:
    """
    field_form = None
    name_field = request.form.get('name_field')
    description_field = request.form.get('description_field')
    type_field = request.form.get('type_field')

    is_real_id_type_field = check_type_field_or_none(type_field=type_field)
    is_str_name_field = isinstance(name_field, str) and name_field
    is_str_description_field = isinstance(description_field, str) and description_field

    if is_real_id_type_field and is_str_name_field and is_str_description_field:
        field_form = FieldForm(name_field=name_field,
                               description=description_field,
                               type_field_id=is_real_id_type_field,
                               form_id=form_id,
                               value_field=None)

    return field_form


def get_form_data_service(form_uid) -> list[tuple] | None:
    return (
        db.session.query(
            Form.id, Form.form_uid, Form.name_form,
            FieldForm.id.label('field_id'), FieldForm.name_field, FieldForm.description, FieldForm.type_field_id,
            FieldForm.value_field.label('value_field'),
            TypeField.id, TypeField.type_field, TypeField.type_value_field
        ).filter(
            Form.id == FieldForm.form_id
        ).filter(
            FieldForm.type_field_id == TypeField.id
        ).filter(
            Form.form_uid == form_uid
        ).all()
    )


def get_fields_form_or_none_template(form_id) -> Optional[FieldForm]:
    return (
        db.session.query(
            FieldForm, TypeField
        ).filter(
            FieldForm.type_field_id == TypeField.id
        ).filter(
            FieldForm.form_id == form_id
        ).all()
    )


def get_list_fields(fields_form_rows: list, need_value_field: bool = True) -> list[dict]:
    """
    Превращение полей формы из SqlAlchemy.Row в list[dict]

    :param fields_form_rows: Объект SqlAlchemy.Row
    :param need_value_fields: Нужно ли поле value_fields
    :return:
    """
    list_form_fields = []

    for fields_form_row in fields_form_rows:

        if need_value_field:
            dict_fields_form = dict(fields_form_row)
        else:
            dict_fields_form = dict(fields_form_row)
            dict_fields_form.pop('value_field')

        list_form_fields.append(dict_fields_form)

    return list_form_fields


def update_value_fields(value_fields: list) -> bool:
    db.session.bulk_update_mappings(FieldForm,
                                    value_fields
                                    )
    try:
        db.session.commit()
        return True
    except StaleDataError as e:
        print(e)
        return False
