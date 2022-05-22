class FieldUtils:
    @staticmethod
    def get_field_matching(type_filed: str) -> str:
        type_dict = {
            'select': 'string',
            'input': 'string',
            'textarea': 'string'
        }
        return type_dict.get(type_filed)
