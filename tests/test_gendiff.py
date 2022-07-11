import pytest
import os
from gendiff import generate_diff


FIXTURE_PATH = os.path.join('tests', 'fixtures')


@pytest.mark.parametrize("file1, file2, format_name, result", [(FIXTURE_PATH + '/file1.json', FIXTURE_PATH + '/file2.yaml',
                                                                'stylish', open(FIXTURE_PATH + '/result_stylish').read()),
                                                               (FIXTURE_PATH + '/file3.json', FIXTURE_PATH + '/file4.yml',
                                                                'stylish', open(FIXTURE_PATH + '/result_stylish_nested').read()),
                                                               (FIXTURE_PATH + '/file1.yml', FIXTURE_PATH + '/file2.json',
                                                                'plain', open(FIXTURE_PATH + '/result_plain').read()),
                                                               (FIXTURE_PATH + '/file3.yml', FIXTURE_PATH + '/file4.json',
                                                                'plain', open(FIXTURE_PATH + '/result_plain_nested').read()),
                                                               (FIXTURE_PATH + '/file1.json', FIXTURE_PATH + '/file2.json',
                                                                'json', open(FIXTURE_PATH + '/result_json.json').read()),
                                                               (FIXTURE_PATH + '/file3.yml', FIXTURE_PATH + '/file4.yml',
                                                                'json', open(FIXTURE_PATH + '/result_json_nested.json').read())])
def test_stylish_formatter(file1, file2, format_name, result):
    assert generate_diff(file1, file2, format_name) == result
