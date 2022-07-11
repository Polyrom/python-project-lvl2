import pytest
import os
from gendiff import generate_diff


FIXTURE_PATH = os.path.join('tests', 'fixtures')


@pytest.mark.parametrize("file1, file2, format_name, result",
                         [('/file1.json', '/file2.yaml', 'stylish', '/result_stylish'),
                          ('/file3.json', '/file4.yml', 'stylish', '/result_stylish_nested'),
                          ('/file1.yml', '/file2.json', 'plain', '/result_plain'),
                          ('/file3.yml', '/file4.json', 'plain', '/result_plain_nested'),
                          ('/file1.json', '/file2.json', 'json', '/result_json.json'),
                          ('/file3.yml', '/file4.yml', 'json', '/result_json_nested.json')])
def test_stylish_formatter(file1, file2, format_name, result):
    assert generate_diff(FIXTURE_PATH + file1, FIXTURE_PATH + file2, format_name) == \
           open(FIXTURE_PATH + result).read()
