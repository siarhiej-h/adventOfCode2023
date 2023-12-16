def part_one(input):
    grid, start_position = input

    next_position = start_position
    known_positions = set()
    steps = 0
    while next_position:
        known_positions.add(next_position)
        next_position = get_next_position(grid, next_position, known_positions)
        steps += 1
    print(steps // 2)


def get_next_position(grid, position, known_positions):
    row, column = position

    can_go_up = {"S", "|", "J", "L"}
    can_go_down = {"S", "|", "7", "F"}
    can_go_right = {"S", "-", "F", "L"}
    can_go_left = {"S", "-", "7", "J"}
    up_routes = {"|", "7", "F"}
    down_routes = {"|", "J", "L"}
    left_routes = {"-", "F", "L"}
    right_routes = {"-", "7", "J"}

    # Check if we can go up
    current_pipe = grid[row][column]
    if current_pipe in can_go_up and row > 0 and grid[row - 1][column] in up_routes:
        next_position = (row - 1, column)
        if next_position not in known_positions:
            return next_position

    # Check if we can go down
    if current_pipe in can_go_down and row < len(grid) - 1 and grid[row + 1][column] in down_routes:
        next_position = (row + 1, column)
        if next_position not in known_positions:
            return next_position

    # Check if we can go left
    if current_pipe in can_go_left and column > 0 and grid[row][column - 1] in left_routes:
        next_position = (row, column - 1)
        if next_position not in known_positions:
            return next_position

    # Check if we can go right
    if current_pipe in can_go_right and column < len(grid[row]) - 1 and grid[row][column + 1] in right_routes:
        next_position = (row, column + 1)
        if next_position not in known_positions:
            return next_position

    return None


def part_two(input):
    grid, start_position = input
    known_loop_positions = set()
    next_position = start_position
    while next_position:
        known_loop_positions.add(next_position)
        next_position = get_next_position(grid, next_position, known_loop_positions)

    enclosed_tiles_count = 0
    grid[start_position[0]][start_position[1]] = "J"
    for row in range(len(grid)):
        enclosed = False
        corner = None
        for col in range(len(grid[row])):
            if (row, col) in known_loop_positions:
                char = grid[row][col]
                if char == "|":
                    enclosed = not enclosed
                elif corner is None and char in ["F", "L"]:
                    corner = char
                elif (corner == "F" and char == "J") or (corner == "L" and char == "7"):
                    enclosed = not enclosed
                    corner = None
                elif (corner == "F" and char == "7") or (corner == "L" and char == "J"):
                    corner = None
                continue
            if enclosed:
                enclosed_tiles_count += 1
    print(enclosed_tiles_count)


def parse_input():
    input_file = "input.txt"
    row_index = 0
    grid = []
    with open(input_file) as f:
        for line in f:
            row = list(line.strip())
            grid.append(row)
            if "S" in row:
                start_position = (row_index, row.index("S"))
            row_index += 1

    return grid, start_position


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
