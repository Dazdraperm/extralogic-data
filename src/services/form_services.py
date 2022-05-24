from typing import Optional

from flask import Request
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

from src import db
from src.models import Form, FieldForm, TypeField


def delete_form_service(form_uid: str) -> int:
    """
    Удаление записи Form по ее form_uid
    :param form_uid:
    :return:
    """
    id_form_deleted = Form.query.filter_by(form_uid=form_uid).delete()
    db.session.commit()

    return id_form_deleted


def get_form_or_none(form_uid) -> Optional[Form]:
    return Form.query.filter_by(form_uid=form_uid).first()


def get_fields_form_or_none(form_id) -> Optional[FieldForm]:
    return (
        db.session.query(
            FieldForm, TypeField
        ).filter(
            FieldForm.type_field_id == TypeField.id
        ).filter(
            FieldForm.form_id == form_id
        ).all()
    )
    # return Form.query.options(joinedload(TypeField.field_form)).filter_by(form_uid=form_uid).first()


def update_validated_form_or_none(validated_instance: Form, form_uid: str) -> Optional[Form]:
    form = Form.query.filter_by(form_uid=form_uid).first()
    result = None

    if form:
        form.form_uid = validated_instance.form_uid
        form.name_form = validated_instance.name_form

        try:
            db.session.commit()
            result = form
        except IntegrityError as e:
            print(e)

    return result


def validate_form_data(request: Request) -> Optional[Form]:
    """
    Проверка, что form_uid и name_form валидируются по заданным условиям


    :return: Form or None
    """

    form_uid = request.form.get('form_uid')
    name_form = request.form.get('name_form')

    form = None

    try:
        form = Form(form_uid=str(form_uid), name_form=str(name_form))
    except ValueError as e:
        print(e)

    return form
