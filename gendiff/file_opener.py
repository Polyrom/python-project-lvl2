import json
import yaml
from .parser import parse_file


def open_file(filepath):
    file = parse_file(filepath)
    if file == 'json':
        return json.load(open(filepath))
    elif file == 'yml':
        return yaml.safe_load(open(filepath))
