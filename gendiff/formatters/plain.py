import json


def to_str(val):
    if isinstance(val, dict):
        return '[complex value]'
    if isinstance(val, bool) or val is None:
        return json.dumps(val)
    if isinstance(val, str):
        return f"'{val}'"
    return val


def preformat_plain(diff, path=''):
    plain_list = []
    for node in diff:
        node_children = node.get('children')
        node_value = node.get('value')
        old_value = node.get('value1')
        new_value = node.get('value2')
        node_key = node.get('key')
        node_type = node.get('type')
        if node_type == 'added':
            plain_list.append(
                f'Property \'{path + node_key}\' '
                f'was added with value: {to_str(node_value)}'
            )
        if node_type == 'removed':
            plain_list.append(f'Property \'{path+node_key}\' was removed')
        if node_type == 'changed':
            plain_list.append(
                f'Property \'{path + node_key}\' was updated. '
                f'From {to_str(old_value)} to {to_str(new_value)}'
            )
        if node_type == 'nested':
            new_path = f'{path}{node_key}.'
            plain_list.append(preformat_plain(node_children, new_path))
    return '\n'.join(plain_list)


def format_plain(diff):
    return preformat_plain(diff)
