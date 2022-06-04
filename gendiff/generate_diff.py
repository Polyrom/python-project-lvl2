import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    file1_set = set(file1)
    file2_set = set(file2)
    diff = dict()
    common_keys = file1_set & file2_set
    file1_unique_keys = file1_set - file2_set
    file2_unique_keys = file2_set - file1_set
    for key in common_keys:
        if key in file1 and file1[key] == file2[key]:
            diff[f'  {key}'] = file1[key]
        else:
            diff[f'- {key}'] = file1[key]
            diff[f'+ {key}'] = file2[key]
    for key in file1_unique_keys:
        diff[f'- {key}'] = file1[key]
    for key in file2_unique_keys:
        diff[f'+ {key}'] = file2[key]
    diff_sorted = dict()
    for key in sorted(
            diff,
            key=lambda item:
            item.replace("- ", "").replace("+ ", "").replace("  ", "")
    ):
        diff_sorted[key] = diff[key]
    diff_string = json.dumps(diff_sorted)
    diff_string_correct = (
        diff_string.replace(',', "\n").replace('"', '')
        .replace('{', '{\n ').replace('}', '\n}')
    )
    return diff_string_correct
