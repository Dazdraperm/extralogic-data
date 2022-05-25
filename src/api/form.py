from typing import Optional

from flask import Response
from flask_jsonrpc import JSONRPCBlueprint

from src.services.field_service import get_list_fields, update_value_fields, get_form_data_service
from src.services.form_services import get_form_or_none

rpc_bp = JSONRPCBlueprint('form', __name__)


@rpc_bp.method('form.get_fields')
def get_fields(form_uid: str) -> Optional[list]:
    fields_form_rows = None
    dict_fields = None

    form = get_form_or_none(form_uid=form_uid)

    if form:
        fields_form_rows = get_form_data_service(form_uid=form_uid)

    if fields_form_rows:
        dict_fields = get_list_fields(fields_form_rows, need_value_field=False)

    return dict_fields


@rpc_bp.method('form.update_value_fields_by_id')
def update_value_fields_by_id(value_fields: list) -> str | None:
    status_update = update_value_fields(value_fields)

    if not status_update:
        result = 'Такого поля не существует'
    else:
        result = 'Успешное соханение'

    return result


@rpc_bp.method('form.get_form_data')
def get_form_data(form_uid: str) -> list | None:
    form_data = get_form_data_service(form_uid)
    dict_form_data = None

    if form_data:
        dict_form_data = get_list_fields(form_data)

    return dict_form_data
