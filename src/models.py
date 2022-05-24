"""
Models DB
"""
from typing import Optional

from sqlalchemy import func
from src import db

model = db.Model


class Form(model):
    """
    Модель Form

    Основные поля:
    form_uid: уникальный id заданный создателем формы
    description: описание формы
    create_date: Дата создания формы
    """

    id = db.Column(db.BigInteger, primary_key=True, autoincrement="ignore_fk")
    form_uid = db.Column(db.String(length=250), unique=True, nullable=True)
    name_form = db.Column(db.String(length=50))

    field_form = db.relationship(
        "FieldForm",
        backref=db.backref("Form", lazy=True),
        cascade="all, delete",
    )
    create_date = db.Column(db.DateTime, server_default=func.now())

    def __init__(self, form_uid: Optional[str], name_form: Optional[str]):
        self.form_uid = form_uid
        self.name_form = name_form

    def __repr__(self):
        return f"form_uid: {self.form_uid}, name_form: {self.name_form}"


class TypeField(model):
    """
    В таблице заданы типы полей, которые можно создать в форме

    :attr type_field: - Тип поля формы (select, input, textarea, etc)
    :attr type_value_field: - Тип значения поля формы (String, Integer, etc)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement="ignore_fk")

    type_field = db.Column(db.String(length=50))
    type_value_field = db.Column(db.String(length=50))
    field_form = db.relationship(
        "FieldForm",
        backref=db.backref("TypeField", lazy=True),
        cascade="all, delete",
    )

    def __init__(self, type_field, type_value_field):
        self.type_field = type_field
        self.type_value_field = type_value_field

    def __repr__(self):
        return (
            f"type_field: {self.type_field}, type_value_field: {self.type_value_field}"
        )


class FieldForm(model):
    id = db.Column(db.Integer, primary_key=True, autoincrement="ignore_fk")

    name_field = db.Column(db.String(length=40))
    description = db.Column(db.String(length=150))

    form_id = db.Column(
        db.Integer, db.ForeignKey("form.id", ondelete="CASCADE"), nullable=False
    )
    type_field_id = db.Column(
        db.Integer, db.ForeignKey("type_field.id", ondelete="SET NULL"), nullable=True
    )

    def __init__(
            self,
            form_id: Optional[int],
            type_field_id: int,
            name_field: str,
            description: str,
    ):
        self.form_id = form_id
        self.type_field_id = type_field_id
        self.name_field = name_field
        self.description = description

    def __repr__(self):
        return (
            f"form_id: {self.form_id}, "
            f"type_field_id: {self.type_field_id}, "
            f"name_field: {self.name_field}, "
            f"description: {self.description}"
        )


class ValueFieldForm(model):
    """
    Данные находящиеся внутри поля формы
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement="ignore_fk")
    field_form_id = db.Column(db.Integer, db.ForeignKey("field_form.id", ondelete="CASCADE"), unique=True)

    field_form_fk = db.relationship(
        "FieldForm", backref=db.backref("ValueFieldForm", uselist=False)
    )
    value_field = db.Column(db.String(length=250))

    def __init__(self, field_form_id: str, value_field: str):
        self.field_form_id = field_form_id
        self.value_field = value_field

    def __repr__(self):
        return (
            f"form_id: {self.form_id}, "
            f"type_field_id: {self.type_field_id}, "
            f"name_field: {self.name_field}, "
            f"description: {self.description}"
        )
