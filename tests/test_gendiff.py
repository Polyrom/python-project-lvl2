import pytest
import os
from gendiff import generate_internal_representation
from gendiff.parser import parse_files
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


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
def file2_yml_nested():
    return parse_files(os.path.join('tests', 'fixtures', 'file4.yml'))


@pytest.fixture
def result_stylish():
    file = open(os.path.join('tests', 'fixtures', 'result_stylish'))
    result = file.read()
    return result


@pytest.fixture
def result_stylish_nested():
    file = open(os.path.join('tests', 'fixtures', 'result_stylish_nested'))
    result_nested = file.read()
    return result_nested


@pytest.fixture
def result_plain():
    file = open(os.path.join('tests', 'fixtures', 'result_plain'))
    result_plain = file.read()
    return result_plain


@pytest.fixture
def result_plain_nested():
    file = open(os.path.join('tests', 'fixtures', 'result_plain_nested'))
    result_plain_nested = file.read()
    return result_plain_nested


@pytest.fixture
def result_json():
    file = open(os.path.join('tests', 'fixtures', 'result_json.json'))
    result_json = file.read()
    return result_json


@pytest.fixture
def result_json_nested():
    file = open(os.path.join('tests', 'fixtures', 'result_json_nested.json'))
    result_json_nested = file.read()
    return result_json_nested


def test_generate_diff_json(file1_json, file2_json, result_stylish):
    assert format_stylish(generate_internal_representation(file1_json, file2_json)) == result_stylish


def test_generate_diff_yaml(file1_yml, file2_yaml, result_stylish):
    assert format_stylish(generate_internal_representation(file1_yml, file2_yaml)) == result_stylish


def test_generate_diff_yaml_json(file1_yml, file2_json, result_stylish):
    assert format_stylish(generate_internal_representation(file1_yml, file2_json)) == result_stylish


def test_generate_diff_nested_json(file1_json_nested, file2_json_nested, result_stylish_nested):
    assert format_stylish(generate_internal_representation(file1_json_nested, file2_json_nested)) == result_stylish_nested


def test_generate_diff_nested_yaml(file1_yml_nested, file2_yml_nested, result_stylish_nested):
    assert format_stylish(generate_internal_representation(file1_yml_nested, file2_yml_nested)) == result_stylish_nested


def test_plain_formatter(file1_json, file2_yaml, result_plain):
    assert format_plain(generate_internal_representation(file1_json, file2_yaml)) == result_plain


def test_plain_formatter_nested(file1_json_nested, file2_yml_nested, result_plain_nested):
    assert format_plain(generate_internal_representation(file1_json_nested, file2_yml_nested)) == result_plain_nested


def test_json_formatter(file1_json, file2_yaml, result_json):
    assert format_json(generate_internal_representation(file1_json, file2_yaml)) == result_json


def test_json_formatter_nested(file1_json_nested, file2_yml_nested, result_json_nested):
    assert format_json(generate_internal_representation(file1_json_nested, file2_yml_nested)) == result_json_nested
