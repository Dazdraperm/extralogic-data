"""
Models DB
"""
from sqlalchemy import Column, Integer, String, BigInteger, ForeignKey, orm
from sqlalchemy.orm import relationship

from .db_worker import DBWorker
from .utils import FieldUtils

db_worker = DBWorker()

db_base = db_worker.get_base()


class Form(db_base):
    __tablename__ = 'Form'

    id = Column(BigInteger, primary_key=True, autoincrement='ignore_fk')
    form_uid = Column(BigInteger, primary_key=True, autoincrement='ignore_fk', nullable=True)
    field_form = relationship("FieldForm", backref="Form", cascade="all, delete", )


class FieldForm(db_base):
    __tablename__ = 'FieldOfForm'

    id = Column(Integer, primary_key=True, autoincrement='ignore_fk')
    form_id = Column(Integer, ForeignKey('Form.id', ondelete="CASCADE"))
    type_field_id = Column(Integer, ForeignKey('TypeField.id', ondelete="None"))


class TypeField(db_base):
    """
    Описание полей таблицы:

    type_field - Тип поля. (select, input, textarea, etc)
    type_value_field - Тип значения поля. (String, Integer, etc)
    """
    __tablename__ = 'TypeField'

    id = Column(Integer, primary_key=True, autoincrement='ignore_fk')

    type_field = String(length=50)
    type_value_field = String(length=50)
    field_form = relationship("FieldForm", backref="Form", cascade="all, delete", )

    # @orm.reconstructor
    # def init_on_load(self, type_field: str):
    #     self.type_field = type_field
    #     self.type_value_field = FieldUtils.get_field_matching(self.type_field)
