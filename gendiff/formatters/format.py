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
