import pytest
import os
from gendiff import generate_diff


file1_json = os.path.join('tests', 'fixtures', 'file1.json')
file2_json = os.path.join('tests', 'fixtures', 'file2.json')
file3_json = os.path.join('tests', 'fixtures', 'file3.json')
file4_json = os.path.join('tests', 'fixtures', 'file4.json')

file1_yml = os.path.join('tests', 'fixtures', 'file1.yml')
file2_yaml = os.path.join('tests', 'fixtures', 'file2.yaml')
file3_yml = os.path.join('tests', 'fixtures', 'file3.yml')
file4_yml = os.path.join('tests', 'fixtures', 'file4.yml')

result_stylish = open(os.path.join('tests', 'fixtures', 'result_stylish')).read()
result_stylish_nested = open(os.path.join('tests', 'fixtures', 'result_stylish_nested')).read()
result_plain = open(os.path.join('tests', 'fixtures', 'result_plain')).read()
result_plain_nested = open(os.path.join('tests', 'fixtures', 'result_plain_nested')).read()
result_json = open(os.path.join('tests', 'fixtures', 'result_json.json')).read()
result_json_nested = open(os.path.join('tests', 'fixtures', 'result_json_nested.json')).read()


@pytest.mark.parametrize("diff, stylish_result", [(generate_diff(file1_json, file2_yaml), result_stylish),
                                                  (generate_diff(file3_json, file4_yml), result_stylish_nested)])
def test_stylish_formatter(diff, stylish_result):
    assert diff == stylish_result


@pytest.mark.parametrize("diff, plain_result", [(generate_diff(file1_yml, file2_json, 'plain'), result_plain),
                                                (generate_diff(file3_yml, file4_json, 'plain'), result_plain_nested)])
def test_plain_formatter(diff, plain_result):
    assert diff == plain_result


@pytest.mark.parametrize("diff, json_result", [(generate_diff(file1_yml, file2_yaml, 'json'), result_json),
                                               (generate_diff(file3_json, file4_yml, 'json'), result_json_nested)])
def test_json_formatter(diff, json_result):
    assert diff == json_result
