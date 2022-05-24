from flask_jsonrpc import JSONRPCBlueprint

from src.services.form_services import get_form_or_none, get_fields_form_or_none

rpc_bp = JSONRPCBlueprint('form', __name__)


@rpc_bp.method('form.get_fields')
def index(form_uid: str):
    fields_form = None

    form = get_form_or_none(form_uid=form_uid)

    if form:
        fields_form_rows = get_fields_form_or_none(form_id=form.id)

    print(dict(fields_form_rows[0]))


    # return dict(fields_form_rows)
