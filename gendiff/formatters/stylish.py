import itertools
import json


ADDED = '+ '
REMOVED = '- '
UNCHANGED = '  '


def preformat_stylish(diff):  # noqa: C901
    prestylish_diff = dict()
    for node in diff:
        node_children = node.get('children')
        node_value = node.get('value')
        node_key = node.get('key')
        node_type = node.get('type')
        if node_type == 'added':
            prestylish_diff[f'{ADDED}{node_key}'] = node_value
        if node_type == 'removed':
            prestylish_diff[f'{REMOVED}{node_key}'] = node_value
        if node_type == 'unchanged':
            prestylish_diff[f'{UNCHANGED}{node_key}'] = node_value
        if node_type == 'changed':
            prestylish_diff[f'{REMOVED}{node_key}'] = node.get("value1")
            prestylish_diff[f'{ADDED}{node_key}'] = node.get("value2")
        if node_type == 'nested':
            prestylish_diff[f'{UNCHANGED}{node_key}'] = \
                preformat_stylish(node_children)
    return prestylish_diff


def format_stylish(value, replacer=' ', spaces_count=4):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if isinstance(val, bool) or val is None:
                val = json.dumps(val)
            if key.startswith(ADDED) or \
                    key.startswith(REMOVED) \
                    or key.startswith(UNCHANGED):
                deep_indent = (replacer * deep_indent_size)[2:]
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(preformat_stylish(value), 0)
