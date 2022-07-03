def generate_diff(dictionary1, dictionary2):
    tree = []
    for key in sorted({**dictionary1, **dictionary2}):
        if isinstance(dictionary1.get(key), dict) and isinstance(dictionary2.get(key), dict):
            node = {
                'key': key,
                'type': 'nested',
                'children': generate_diff(dictionary1.get(key), dictionary2.get(key))
            }
            tree.append(node)
        else:
            if key in dictionary1 and key not in dictionary2:
                node = {
                    'key': key,
                    'type': 'removed',
                    'value': dictionary1.get(key)
                }
                tree.append(node)
            elif key in dictionary2 and key not in dictionary1:
                node = {
                    'key': key,
                    'type': 'added',
                    'value': dictionary2.get(key)
                }
                tree.append(node)
            elif dictionary1.get(key) == dictionary2.get(key):
                node = {
                    'key': key,
                    'type': 'unchanged',
                    'value': dictionary1.get(key)
                }
                tree.append(node)
            else:
                node = {
                    'key': key,
                    'type': 'changed',
                    'value1': dictionary1.get(key),
                    'value2': dictionary2.get(key)
                }
                tree.append(node)
    return tree
