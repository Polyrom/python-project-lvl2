import json
import yaml
from pathlib import Path


def parse_files(filepath):
    filename = Path(filepath)
    if filename.suffix == '.json':
        return json.load(open(filepath))
    if filename.suffix == '.yml' or filename.suffix == '.yaml':
        return yaml.safe_load(open(filepath))
