import json


ADDED = 'Added: '
REMOVED = 'Removed: '
UNCHANGED = 'Unchanged: '
NESTED = 'Nested: '


def preformat_json(diff):  # noqa: C901
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
            prestylish_diff[f'{NESTED}{node_key}'] = \
                preformat_json(node_children)
    return prestylish_diff


def format_json(diff):
    diff_in_dict = preformat_json(diff)
    return json.dumps(diff_in_dict, indent=4)
