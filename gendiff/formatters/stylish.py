import itertools
import json


ADDED = '+ '
REMOVED = '- '
UNCHANGED = '  '
INDENT = '    '


def preformat_stylish(diff):
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
            prestylish_diff[f'{UNCHANGED}{node_key}'] = preformat_stylish(node_children)
    return prestylish_diff


def format_stylish(value, replacer=' ', spaces_count=2):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent = replacer * spaces_count
        current_indent = replacer * spaces_count * depth
        if depth > 0:
            deep_indent = (depth * INDENT) + (replacer * spaces_count)
        lines = []
        for key, val in current_value.items():
            if isinstance(val, bool) or val is None:
                val = json.dumps(val)
            lines.append(f'{deep_indent}{key}: {iter_(val, depth + 1)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(preformat_stylish(value), 0)
