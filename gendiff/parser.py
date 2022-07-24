import os
import json
import yaml


def parse(data, format_name):
    if format_name == 'json':
        return json.load(open(data))
    if format_name == 'yml' or format_name == 'yaml':
        return yaml.safe_load(open(data))
    raise Exception("Wrong format name. "
                    "Make sure your files are JSON or YAML/YML.")


def get_content(filepath):
    _, extension = os.path.splitext(filepath)
    file_format = extension.replace('.', '')
    return parse(filepath, file_format)
