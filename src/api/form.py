from typing import Optional

from flask_jsonrpc import JSONRPCBlueprint

from src.services.field_service import get_dict_fields, get_fields_form_or_none
from src.services.form_services import get_form_or_none

rpc_bp = JSONRPCBlueprint('form', __name__)


@rpc_bp.method('form.get_fields')
def get_fields(form_uid: str) -> Optional[dict]:
    fields_form_rows = None
    dict_fields = None

    form = get_form_or_none(form_uid=form_uid)

    if form:
        fields_form_rows = get_fields_form_or_none(form_id=form.id)

    if fields_form_rows:
        dict_fields = get_dict_fields(fields_form_rows)

    return dict_fields
