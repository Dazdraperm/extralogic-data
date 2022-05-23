from typing import Optional

from psycopg2 import IntegrityError

from src import db


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


def save_validate_instance_or_error(
        validate_instance: db.Model,
        save_error: str
) -> (Optional[db.Model], Optional[str]):
    """
    Если существуют валидные данные, то пытаемся сохранить данный instance, если не получилось сохранить,
    то выдаем ошибку сохранения

    :param validate_instance: instance, который надо сохранить
    :param save_error: какую выдать ошибку, если не удалось сохранить
    :return:
    """
    saved_instance = None
    error = None
    validate_data_error = "Вы ввели не валидные данные"

    if validate_instance:
        saved_instance = insert_validated_instance_or_none(
            validated_instance=validate_instance
        )
    else:
        error = validate_data_error

    if saved_instance is None:
        error = save_error

    return saved_instance, error
