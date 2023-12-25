from collections import defaultdict
from collections import deque
from copy import deepcopy


def parse_input():
    input_file = "input.txt"
    graph = defaultdict(list)
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            parts = line.split(": ")
            name = parts[0]
            others = parts[1].split(" ")
            for other in others:
                graph[name].append(other)
                graph[other].append(name)

    return graph


def bfs(graph, start):
    nodes = deque([start])
    visited = {start: None}
    node = None
    while nodes:
        node = nodes.popleft()
        for next_node in graph[node]:
            if next_node not in visited:
                visited[next_node] = node
                nodes.append(next_node)

    path = []
    end = node
    while end is not None:
        path.append(end)
        end = visited[end]
    return path, len(visited)


def edmond_karp(graph, cuts):
    graph = deepcopy(graph)
    start = next(iter(graph.keys()))
    for i in range(cuts):
        path, _ = bfs(graph, start)
        remove_path(graph, path)
    _, reachable = bfs(graph, start)
    return reachable


def remove_path(graph, path):
    left_node = path[0]
    for j in range(1, len(path)):
        right_node = path[j]
        graph[left_node].remove(right_node)
        graph[right_node].remove(left_node)
        left_node = right_node


def part_one(input):
    graph = input
    reachable = edmond_karp(graph, 3)
    total = len(graph)
    print(reachable * (total - reachable))


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
