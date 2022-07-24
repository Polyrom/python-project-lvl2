import pytest
import os
from gendiff import generate_diff


def build_fixture_path(filename):
    return os.path.join('tests', 'fixtures', filename)


@pytest.mark.parametrize("file1, file2, format_name, result",
                         [('file1.json', 'file2.yaml', 'stylish', 'result_stylish'),
                          ('file3.json', 'file4.yml', 'stylish', 'result_stylish_nested'),
                          ('file1.yml', 'file2.json', 'plain', 'result_plain'),
                          ('file3.yml', 'file4.json', 'plain', 'result_plain_nested'),
                          ('file1.json', 'file2.json', 'json', 'result_json.json'),
                          ('file3.yml', 'file4.yml', 'json', 'result_json_nested.json')])
def test_stylish_formatter(file1, file2, format_name, result):
    assert generate_diff(build_fixture_path(file1), build_fixture_path(file2), format_name) == \
           open(build_fixture_path(result)).read()
