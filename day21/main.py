from collections import deque


def parse_input():
    input_file = "input.txt"
    grid = []
    start = None
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))
            if "S" in line:
                start = (len(grid) - 1, line.index("S"))

    return grid, start


def part_one(input):
    grid, start = input
    reachable_plots = traverse(grid, start, 64, infinite_grid=False)
    print(reachable_plots)


def traverse(grid, start, steps_left, infinite_grid=False):
    start_row, start_column = start
    queue = deque([(start_row, start_column, steps_left)])
    end_coordinates = 0
    visited = set()
    while queue:
        row, column, steps = queue.popleft()
        if (row, column, steps) in visited:
            continue
        visited.add((row, column, steps))

        if steps == 0:
            end_coordinates += 1
            continue

        steps -= 1
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            new_row = row + dr
            new_column = column + dc
            if is_valid(grid, new_row, new_column, infinite_grid):
                queue.append((new_row, new_column, steps))

    return end_coordinates


def is_valid(grid, row, column, infinite_grid):
    if infinite_grid:
        while row < 0:
            row += len(grid)
        while column < 0:
            column += len(grid[0])
        while row >= len(grid):
            row -= len(grid)
        while column >= len(grid[0]):
            column -= len(grid[0])
    return 0 <= row < len(grid) and 0 <= column < len(grid[0]) and grid[row][column] != "#"


def part_two(input):
    grid, start = input
    # reachable plots = f(x) where x is how many times grid is expanded
    # 26501365 = 65 + 131 * expansions
    target_x = 26501365 // 131
    # f(x) = a + b * x + c * x^2
    # y0 = f(0)
    # a = y0
    y0 = traverse(grid, start, 65, infinite_grid=True)
    a = y0

    # y1 = f(1)
    # a + b + c = y1
    # b + c = y1 - a
    # 2b + 2c = 2y1 - 2a

    # y2 = f(2)
    # a + 2b + 4c = y2
    # 2b + 4c = y2 - a
    # c = ((y2 - a) - (2y1 - 2a)) / 2
    # c = (y2 - 2y1 + a) / 2
    # b = y1 - a - c

    y1 = traverse(grid, start, 65 + 131, infinite_grid=True)
    y2 = traverse(grid, start, 65 + 131 * 2, infinite_grid=True)
    c = (y2 - 2 * y1 + a) // 2
    b = y1 - a - c
    reachable_plots = a + b * target_x + c * target_x ** 2
    print(reachable_plots)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
