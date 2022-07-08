from pathlib import Path, PurePath


def parse_file(filepath):
    file_split = PurePath(filepath).parts
    filename = Path(*file_split)
    if filename.suffix == '.json':
        file = 'json'
    elif filename.suffix == '.yaml' \
            or filename.suffix == '.yml':
        file = 'yml'
    else:
        raise Exception("Wrong file format. "
                        "Make sure compared files are JSON or YAML/YML.")
    return file
