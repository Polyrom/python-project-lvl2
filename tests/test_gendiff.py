import pytest
import os
from gendiff import generate_diff


@pytest.fixture
def file1_json():
    return os.path.join('tests', 'fixtures', 'file1.json')


@pytest.fixture
def file2_json():
    return os.path.join('tests', 'fixtures', 'file2.json')


@pytest.fixture
def file1_yml():
    return os.path.join('tests', 'fixtures', 'file1.yml')


@pytest.fixture
def file2_yaml():
    return os.path.join('tests', 'fixtures', 'file2.yaml')


@pytest.fixture
def result():
    file = open(os.path.join('tests', 'fixtures', 'expected_result.txt'))
    result = file.read()
    return result


def test_generate_diff_json(file1_json, file2_json, result):
    assert generate_diff(file1_json, file2_json) == result


def test_generate_diff_yaml(file1_yml, file2_yaml, result):
    assert generate_diff(file1_yml, file2_yaml) == result


def test_generate_diff_yaml_json(file1_yml, file2_json, result):
    assert generate_diff(file1_yml, file2_json) == result
