import json
import yaml
from pathlib import Path, PurePath


def parse_files(filepath):
    file_split = PurePath(filepath).parts
    filename = Path(*file_split)
    if filename.suffix == '.json':
        return json.load(open(filepath))
    if filename.suffix == '.yml' or filename.suffix == '.yaml':
        return yaml.safe_load(open(filepath))
