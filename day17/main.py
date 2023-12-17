from sortedcontainers import SortedList


def parse_input():
    input_file = "input.txt"
    grid = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            grid.append([int(v) for v in line])
    return grid


def traverse(grid, start_position, end_position, min_steps, max_steps):
    state = (0, start_position[0], start_position[1], None)
    visited = dict()
    states = SortedList([state])
    min_heat = None
    while states:
        state = states.pop(0)
        next_states = get_next_states(grid, state, min_steps, max_steps)
        for next_state in next_states:
            heat, row, column, direction = next_state
            if row == end_position[0] and column == end_position[1]:
                if min_heat is None or heat < min_heat:
                    min_heat = heat
                continue

            known_heat = visited.get((row, column, direction), None)
            if known_heat is None or heat < known_heat:
                visited[(row, column, direction)] = heat
                states.add(next_state)

    return min_heat


def get_next_states(grid, state, min_steps, max_steps):
    heat, row, column, direction = state
    next_states = []

    next_direction = "up"
    for i in range(min_steps, max_steps + 1):
        next_row = row - i
        if next_row >= 0 and can_move(direction, next_direction):
            next_heat = heat + sum(grid[j][column] for j in range(next_row, row))
            next_state = (next_heat, next_row, column, next_direction)
            next_states.append(next_state)
        else:
            break

    next_direction = "down"
    for i in range(min_steps, max_steps + 1):
        next_row = row + i
        if next_row < len(grid) and can_move(direction, next_direction):
            next_heat = heat + sum(grid[j][column] for j in range(row + 1, next_row + 1))
            next_state = (next_heat, next_row, column, next_direction)
            next_states.append(next_state)
        else:
            break

    next_direction = "left"
    for i in range(min_steps, max_steps + 1):
        next_column = column - i
        if next_column >= 0 and can_move(direction, next_direction):
            next_heat = heat + sum(grid[row][next_column:column])
            next_state = (next_heat, row, next_column, next_direction)
            next_states.append(next_state)
        else:
            break

    next_direction = "right"
    for i in range(min_steps, max_steps + 1):
        next_column = column + i
        if next_column < len(grid[row]) and can_move(direction, next_direction):
            next_heat = heat + sum(grid[row][column + 1: next_column + 1])
            next_state = (next_heat, row, next_column, next_direction)
            next_states.append(next_state)
        else:
            break

    return next_states


def can_move(previous_direction, direction):
    if previous_direction == direction:
        return False

    if previous_direction == "up" and direction == "down":
        return False

    if previous_direction == "down" and direction == "up":
        return False

    if previous_direction == "left" and direction == "right":
        return False

    if previous_direction == "right" and direction == "left":
        return False

    return True


def part_one(input):
    start_position = (0, 0)
    end_position = (len(input) - 1, len(input[0]) - 1)
    min_heat = traverse(input, start_position, end_position, 1, 3)
    print(min_heat)


def part_two(input):
    start_position = (0, 0)
    end_position = (len(input) - 1, len(input[0]) - 1)
    min_heat = traverse(input, start_position, end_position, 4, 10)
    print(min_heat)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
