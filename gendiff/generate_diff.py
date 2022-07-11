from .tree import build_diff
from .parser import get_content
from gendiff.formatters.format import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = get_content(file_path1)
    file2 = get_content(file_path2)
    internal_diff = build_diff(file1, file2)
    return format_diff(internal_diff, format_name)
