import pytest
import os
from gendiff.gen_diff import generate_diff


@pytest.fixture
def file1():
    return os.path.join('tests', 'fixtures', 'file1.json')


@pytest.fixture
def file2():
    return os.path.join('tests', 'fixtures', 'file2.json')


@pytest.fixture
def result():
    file = open(os.path.join('tests', 'fixtures', 'result_plain_json.txt'))
    result = file.read()
    return result


def test_generate_diff(file1, file2, result):
    assert generate_diff(file1, file2) == result
