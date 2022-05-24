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
    name_field = request.form.get('name_field')
    description_field = request.form.get('description_field')
    type_field = request.form.get('type_field')

    id_type_field = check_type_field_or_none(type_field=type_field)

    if not id_type_field:
        return None

    try:
        field_form = FieldForm(name_field=str(name_field),
                               description=str(description_field),
                               type_field_id=id_type_field,
                               form_id=form_id,
                               value_field=None)
    except ValueError as e:
        print(e)
        return None

    return field_form


def get_fields_form_or_none(form_id) -> Optional[FieldForm]:
    return (
        db.session.query(
            FieldForm.form_id, FieldForm.id.label('field_id'), FieldForm.name_field, FieldForm.description,
            TypeField.type_field
        ).filter(
            FieldForm.type_field_id == TypeField.id
        ).filter(
            FieldForm.form_id == form_id
        ).all()
    )


def get_form_data_service(form_uid) -> list[tuple] | None:
    return (
        db.session.query(
            Form.id, Form.form_uid, Form.name_form, FieldForm.id.label('field_id'), FieldForm.name_field,
            FieldForm.description,
            FieldForm.type_field_id, FieldForm.value_field, TypeField.type_field, TypeField.type_value_field,
            TypeField.id
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


def get_dict_fields(fields_form_rows: list) -> dict:
    dict_form_fields = {}

    for fields_form_row in fields_form_rows:
        dict_form_fields[fields_form_row.field_id] = dict(fields_form_row)

    return dict_form_fields


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
