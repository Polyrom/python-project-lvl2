import pytest
import os
from gendiff.scripts.gendiff import main


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


def test_main_json(capsys, file1_json, file2_json, result):
    print(main([file1_json, file2_json]), end='')
    captured = capsys.readouterr()
    assert captured.out == result


def test_main_yaml(capsys, file1_yml, file2_yaml, result):
    print(main([file1_yml, file2_yaml]), end='')
    captured = capsys.readouterr()
    assert captured.out == result
