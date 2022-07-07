import json


def format_value(val):
    if isinstance(val, dict):
        new_val = '[complex value]'
        return new_val
    elif isinstance(val, bool) or val is None:
        new_val = json.dumps(val)
        return new_val
    elif isinstance(val, str):
        new_val = f"'{val}'"
        return new_val
    else:
        return val


def format_plain(diff, path=''):
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
                f'was added with value: {format_value(node_value)}'
            )
        if node_type == 'removed':
            plain_list.append(f'Property \'{path+node_key}\' was removed')
        if node_type == 'changed':
            plain_list.append(
                f'Property \'{path + node_key}\' was updated. '
                f'From {format_value(old_value)} to {format_value(new_value)}'
            )
        if node_type == 'nested':
            new_path = f'{path}{node_key}.'
            plain_list.append(format_plain(node_children, new_path))
    return '\n'.join(plain_list)
