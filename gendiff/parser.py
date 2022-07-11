import os
import json
import yaml


def parse_files(data, format_name):
    if format_name == 'json':
        return json.load(open(data))
    elif format_name == 'yml':
        return yaml.safe_load(open(data))


def get_content(filepath):
    path, extension = os.path.splitext(filepath)
    if extension == '.json':
        return parse_files(filepath, 'json')
    elif extension == '.yaml' \
            or extension == '.yml':
        return parse_files(filepath, 'yml')
    else:
        raise Exception("Wrong file format. "
                        "Make sure compared files are JSON or YAML/YML.")
