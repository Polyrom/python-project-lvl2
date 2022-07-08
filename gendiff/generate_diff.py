from .tree import make_diff_tree
from .file_opener import open_file
from gendiff.formatters.format import format_diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)
    internal_diff = make_diff_tree(file1, file2)
    return format_diff(internal_diff, format_name)
