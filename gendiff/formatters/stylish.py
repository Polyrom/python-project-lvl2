import itertools
import json


PREFIXES = {
    'added': '+ ',
    'removed': '- ',
    'unchanged': '  '
}


def preformat_stylish(diff):
    prestylish_diff = dict()
    for node in diff:
        node_children = node.get('children')
        node_value = node.get('value')
        node_key = node.get('key')
        node_type = node.get('type')
        old_value = node.get("value1")
        new_value = node.get("value2")
        if node_type == 'changed':
            prestylish_diff[f'{PREFIXES["removed"]}{node_key}'] = old_value
            prestylish_diff[f'{PREFIXES["added"]}{node_key}'] = new_value
        elif node_type == 'nested':
            prestylish_diff[f'{PREFIXES["unchanged"]}{node_key}'] = \
                preformat_stylish(node_children)
        else:
            prestylish_diff[f'{PREFIXES[node_type]}{node_key}'] = node_value
    return prestylish_diff


def to_str(value):
    if isinstance(value, bool) or value is None:
        return json.dumps(value)
    return value


def iter_(tree, depth, replacer=' ', spaces_count=4):
    if not isinstance(tree, dict):
        return str(tree)
    deep_indent_size = depth + spaces_count
    deep_indent = replacer * deep_indent_size
    current_indent = replacer * depth
    lines = []
    for key, val in tree.items():
        if key.startswith(tuple(prefix for prefix in PREFIXES.values())):
            deep_indent = (replacer * deep_indent_size)[2:]
        lines.append(f'{deep_indent}{key}: '
                     f'{iter_(to_str(val), deep_indent_size)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def format_stylish(diff_tree):
    return iter_(preformat_stylish(diff_tree), 0)
