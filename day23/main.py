from collections import deque

def parse_input():
    input_file = "input.txt"
    grid = []
    with open(input_file) as f:
        index = -1
        for line in f:
            index += 1
            line = line.strip()
            grid.append(list(line))

    return grid


def part_one(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    max_distance = traverse_p1(input, start, end)
    print(max_distance)


def traverse_p1(grid, start, end):
    position = start
    next_states = deque([(position, position, 0)])
    max_distance = 0
    while next_states:
        came_from, position, distance = next_states.popleft()
        if position == end:
            max_distance = max(max_distance, distance)
            continue

        row, col = position
        directions = get_valid_directions_p1(grid, row, col)
        for dr, dc in directions:
            next_position = (row + dr, col + dc)
            if next_position == came_from:
                continue

            next_states.append((position, next_position, distance + 1))
    return max_distance


def get_valid_directions_p1(grid, row, col):
    if grid[row][col] == ">":
        yield 0, 1
    elif grid[row][col] == "<":
        yield 0, -1
    elif grid[row][col] == "^":
        yield -1, 0
    elif grid[row][col] == "v":
        yield 1, 0
    else:
        if row > 0 and grid[row - 1][col] not in ["#", "v"]:
            yield -1, 0

        if row < len(grid) - 1 and grid[row + 1][col] not in ["#", "^"]:
            yield 1, 0

        if col > 0 and grid[row][col - 1] not in ["#", ">"]:
            yield 0, -1

        if col < len(grid[0]) - 1 and grid[row][col + 1] not in ["#", "<"]:
            yield 0, 1


def part_two(input):
    start = (0, 1)
    end = (len(input) - 1, len(input[0]) - 2)
    graph = build_graph(input)
    visited = set()
    max_distance = traverse_p2(start, end, visited, 0, graph)
    print(max_distance)


class Node:
    def __init__(self, position, neighbors):
        self.position = position
        self.neighbors = {pos: 1 for pos in neighbors}


def build_graph(grid):
    graph = {}
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "#":
                continue

            directions = get_valid_directions_p2(grid, row, col)
            neighbours = [(row + dr, col + dc) for dr, dc in directions]
            node = Node((row, col), neighbours)
            graph[(row, col)] = node

    collapse_nodes_with_two_neighbors(graph)
    return graph


def collapse_nodes_with_two_neighbors(graph):
    nodes_with_two_neighbours = [node for _, node in graph.items() if len(node.neighbors) == 2]
    for node in nodes_with_two_neighbours:
        node1_position, node2_position = node.neighbors
        node1 = graph[node1_position]
        node2 = graph[node2_position]

        node1.neighbors[node2.position] = node.neighbors[node2.position] + node1.neighbors[node.position]
        node2.neighbors[node1.position] = node1.neighbors[node2.position]

        del node1.neighbors[node.position]
        del node2.neighbors[node.position]
        del graph[node.position]


def traverse_p2(position, end, visited, distance, graph):
    if position == end:
        return distance

    visited.add(position)
    max_distance = 0
    for neighbour_position, neighbour_distance in graph[position].neighbors.items():
        if neighbour_position not in visited:
            max_distance = max(max_distance, traverse_p2(neighbour_position, end, visited, distance + neighbour_distance, graph))
    visited.remove(position)
    return max_distance


def get_valid_directions_p2(grid, row, col):
    if row > 0 and grid[row - 1][col] != "#":
        yield -1, 0

    if row < len(grid) - 1 and grid[row + 1][col] != "#":
        yield 1, 0

    if col > 0 and grid[row][col - 1] != "#":
        yield 0, -1

    if col < len(grid[0]) - 1 and grid[row][col + 1] != "#":
        yield 0, 1


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
