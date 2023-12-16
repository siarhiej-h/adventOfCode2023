def parse_input():
    input_file = "input.txt"
    rows = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            rows.append(list(line))
    return rows


def move_grid_north(grid):
    for i in range(1, len(grid)):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            if tile == "O":
                k = i
                while k - 1 >= 0 and grid[k - 1][j] == ".":
                    k -= 1
                grid[i][j] = "."
                grid[k][j] = "O"


def move_grid_south(grid):
    for i in range(len(grid) - 2, -1, -1):
        for j in range(len(grid[i])):
            tile = grid[i][j]
            if tile == "O":
                k = i
                while k + 1 < len(grid) and grid[k + 1][j] == ".":
                    k += 1
                grid[i][j] = "."
                grid[k][j] = "O"


def move_grid_east(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 2, -1, -1):
            tile = grid[i][j]
            if tile == "O":
                k = j
                while k + 1 < len(grid[i]) and grid[i][k + 1] == ".":
                    k += 1
                grid[i][j] = "."
                grid[i][k] = "O"


def move_grid_west(grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            tile = grid[i][j]
            if tile == "O":
                k = j
                while k - 1 >= 0 and grid[i][k - 1] == ".":
                    k -= 1
                grid[i][j] = "."
                grid[i][k] = "O"


def part_one(input):
    move_grid_north(input)
    load = get_load(input)
    print(load)


def run_cycle(input):
    move_grid_north(input)
    move_grid_west(input)
    move_grid_south(input)
    move_grid_east(input)


def part_two(input):
    cycles_required = 1000000000
    states = set()
    while True:
        cycles_required -= 1
        run_cycle(input)
        state = "".join(["".join(row) for row in input])
        if state in states:
            break
        states.add(state)

    states.clear()

    frequency = 0
    while True:
        cycles_required -= 1
        run_cycle(input)
        state = "".join(["".join(row) for row in input])
        if state in states:
            break
        states.add(state)
        frequency += 1

    for i in range(0, cycles_required % frequency):
        run_cycle(input)

    print(get_load(input))


def get_load(input):
    load = 0
    for i in range(len(input)):
        row = input[i]
        load_coefficient = len(input) - i
        for char in row:
            if char == "O":
                load += load_coefficient
    return load


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
