def solve_part_one(data):
    counter = 0
    for node1, node2 in data:
        num_paths = 0
        if node1 == 'start':
            num_paths = find_path(node2, ['start'], data)
        elif node2 == 'start':
            num_paths = find_path(node1, ['start'], data)
        counter += num_paths
    return counter


def find_path(node, path, data):
    if node == 'end':
        return 1

    if node_allowed(node, path):
        path.append(node)
    else:
        return 0

    counter = 0
    for node1, node2 in data:
        num_paths = 0
        if node == node1:
            num_paths = find_path(node2, path, data)
        elif node == node2:
            num_paths = find_path(node1, path, data)
        counter += num_paths

    # if reached, no adjacent node was found
    path.pop(-1)

    return counter
            
def node_allowed(node, path):
    if node.islower() and node in path:
        return False
    return True


with open('input.txt') as f:
    data = [path.strip().split('-') for path in f]

result = solve_part_one(data)
print('Part 1:', result)
