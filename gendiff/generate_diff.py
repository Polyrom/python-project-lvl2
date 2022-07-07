from .internal_representation import generate_internal_representation
from .parser import parse_files
from .formatters.stylish import format_stylish
from .formatters.plain import format_plain
from .formatters.json import format_json


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = parse_files(file_path1)
    file2 = parse_files(file_path2)
    internal_diff = generate_internal_representation(file1, file2)
    if format_name == 'stylish':
        return format_stylish(internal_diff)
    elif format_name == 'plain':
        return format_plain(internal_diff)
    elif format_name == 'json':
        return format_json(internal_diff)
