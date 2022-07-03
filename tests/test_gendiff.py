import pytest
import os
from gendiff import generate_diff
from gendiff.parser import parse_files
from gendiff.formatters.stylish import format_stylish


@pytest.fixture
def file1_json():
    return parse_files(os.path.join('tests', 'fixtures', 'file1.json'))


@pytest.fixture
def file2_json():
    return parse_files(os.path.join('tests', 'fixtures', 'file2.json'))


@pytest.fixture
def file1_yml():
    return parse_files(os.path.join('tests', 'fixtures', 'file1.yml'))


@pytest.fixture
def file2_yaml():
    return parse_files(os.path.join('tests', 'fixtures', 'file2.yaml'))


@pytest.fixture
def file1_json_nested():
    return parse_files(os.path.join('tests', 'fixtures', 'file3.json'))


@pytest.fixture
def file2_json_nested():
    return parse_files(os.path.join('tests', 'fixtures', 'file4.json'))


@pytest.fixture
def file1_yml_nested():
    return parse_files(os.path.join('tests', 'fixtures', 'file3.yml'))


@pytest.fixture
def file2_yaml_nested():
    return parse_files(os.path.join('tests', 'fixtures', 'file4.yaml'))


@pytest.fixture
def result():
    file = open(os.path.join('tests', 'fixtures', 'expected_result_plain.txt'))
    result = file.read()
    return result


@pytest.fixture
def result_nested():
    file = open(os.path.join('tests', 'fixtures', 'expected_result_tree.txt'))
    result_nested = file.read()
    return result_nested


def test_generate_diff_json(file1_json, file2_json, result):
    assert format_stylish(generate_diff(file1_json, file2_json)) == result


def test_generate_diff_yaml(file1_yml, file2_yaml, result):
    assert format_stylish(generate_diff(file1_yml, file2_yaml)) == result


def test_generate_diff_yaml_json(file1_yml, file2_json, result):
    assert format_stylish(generate_diff(file1_yml, file2_json)) == result


def test_generate_diff_nested_json(file1_json_nested, file2_json_nested, result_nested):
    assert format_stylish(generate_diff(file1_json_nested, file2_json_nested)) == result_nested


def test_generate_diff_nested_yaml(file1_yml_nested, file2_yaml_nested, result_nested):
    assert format_stylish(generate_diff(file1_yml_nested, file2_yaml_nested)) == result_nested
