from flask import Request
from sqlalchemy.exc import IntegrityError

from src import db
from src.models import Form


def insert_validated_instance_or_none(validated_instance: db.Model) -> (db.Model, None):
    """
    Создание обьекта из инстанса

    :param validated_instance:
    :return:
    """
    try:
        db.session.add(validated_instance)
        db.session.commit()
    except IntegrityError:
        return None

    return validated_instance


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
