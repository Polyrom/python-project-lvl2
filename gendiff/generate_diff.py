from .tree import make_diff_tree
from .file_opener import open_file


def generate_diff(file_path1, file_path2):
    file1 = open_file(file_path1)
    file2 = open_file(file_path2)
    internal_diff = make_diff_tree(file1, file2)
    return internal_diff
