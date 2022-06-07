import json
import yaml


def parse_files(filepath):
    if filepath.endswith('.json'):
        return json.load(open(filepath))
    if filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return yaml.safe_load(open(filepath))
