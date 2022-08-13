def build_diff(data1, data2):
    tree = {}
    for key in sorted({**data1, **data2}):
        if isinstance(data1.get(key), dict) \
                and isinstance(data2.get(key), dict):
            node = {
                'type': 'nested',
                'children': build_diff(data1.get(key), data2.get(key))
            }
            tree[key] = node
        else:
            if key in data1 and key not in data2:
                node = {
                    'type': 'removed',
                    'value': data1.get(key)
                }
                tree[key] = node
            elif key in data2 and key not in data1:
                node = {
                    'type': 'added',
                    'value': data2.get(key)
                }
                tree[key] = node
            elif data1.get(key) == data2.get(key):
                node = {
                    'type': 'unchanged',
                    'value': data1.get(key)
                }
                tree[key] = node
            else:
                node = {
                    'type': 'changed',
                    'value1': data1.get(key),
                    'value2': data2.get(key)
                }
                tree[key] = node
    return tree
