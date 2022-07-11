from .stylish import format_stylish
from .plain import format_plain
from .json import format_json


def format_diff(diff, formatter):
    if formatter == 'stylish':
        return format_stylish(diff)
    elif formatter == 'plain':
        return format_plain(diff)
    elif formatter == 'json':
        return format_json(diff)
    else:
        raise Exception('Invalid format name.'
                        'Please select from "stylish", "plain" and "json".'
                        'See "gendiff -h" for further info.')
