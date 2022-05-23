from flask import Request
from sqlalchemy.exc import IntegrityError

from src import db
from src.models import Form


def update_validated_form_or_none(validated_instance: Form, form_uid: str) -> (Form, None):
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


def insert_validated_instance_or_none(validated_instance: db.Model) -> (db.Model, None):
    """
    Создание обьекта из инстанса

    :param validated_instance:
    :return:
    """
    result = None
    db.session.add(validated_instance)

    try:
        db.session.commit()
        result = validated_instance
    except IntegrityError as e:
        print(e)
    return result


def validate_form_data(request: Request) -> (Form, None):
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
