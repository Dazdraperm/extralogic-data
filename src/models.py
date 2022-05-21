"""
Models DB
"""
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

    id = db.Column(db.BigInteger, primary_key=True, autoincrement='ignore_fk')
    form_uid = db.Column(db.String(length=250), unique=True, autoincrement='ignore_fk', nullable=True)
    name_form = db.Column(db.String(length=50))

    field_form = db.relationship("FieldForm", backref=db.backref("Form", lazy=True), cascade="all, delete", )
    description = db.Column(db.String(length=150))
    create_date = db.Column(db.DateTime, server_default=func.now())


class TypeField(model):
    """
    Описание полей таблицы:

    type_field - Тип поля. (select, input, textarea, etc)
    type_value_field - Тип значения поля. (String, Integer, etc)
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')

    type_field = db.Column(db.String(length=50))
    type_value_field = db.Column(db.String(length=50))
    field_form = db.relationship("FieldForm", backref=db.backref("TypeField", lazy=True), cascade="all, delete", )


class FieldForm(model):
    id = db.Column(db.Integer, primary_key=True, autoincrement='ignore_fk')
    form_id = db.Column(db.Integer, db.ForeignKey('form.id', ondelete="CASCADE"), nullable=False)
    type_field_id = db.Column(db.Integer, db.ForeignKey('type_field.id', ondelete="SET NULL"), nullable=True)

    # @orm.reconstructor
    # def init_on_load(self, type_field: str):
    #     self.type_field = type_field
    #     self.type_value_field = FieldUtils.get_field_matching(self.type_field)
