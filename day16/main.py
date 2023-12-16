def parse_input():
    input_file = "input.txt"
    grid = []
    with open(input_file) as f:
      for line in f:
        line = line.strip()
        grid.append(list(line))
    return grid


def move_light(grid, impulses, light_map):
    while impulses:
        position, direction = impulses.pop()
        if direction == "right":
            row, column = position
            next_column = column + 1
            if next_column >= len(grid[row]):
                continue

            next_position = (row, next_column)
            if next_position not in light_map:
                light_map[next_position] = ["right"]
            else:
                directions = light_map[next_position]
                if "right" not in directions:
                    directions.append("right")
                else:
                    continue

            next_tile = grid[row][next_column]
            if next_tile in ["-", "."]:
                impulses.append((next_position, direction))
            elif next_tile == "/":
                impulses.append((next_position, "up"))
            elif next_tile == "\\":
                impulses.append((next_position, "down"))
            elif next_tile == "|":
                impulses.append((next_position, "up"))
                impulses.append((next_position, "down"))

        if direction == "left":
            row, column = position
            next_column = column - 1
            if next_column < 0:
                continue

            next_position = (row, next_column)
            if next_position not in light_map:
                light_map[next_position] = ["left"]
            else:
                directions = light_map[next_position]
                if "left" not in directions:
                    directions.append("left")
                else:
                    continue

            next_tile = grid[row][next_column]
            if next_tile in ["-", "."]:
                impulses.append((next_position, direction))
            elif next_tile == "/":
                impulses.append((next_position, "down"))
            elif next_tile == "\\":
                impulses.append((next_position, "up"))
            elif next_tile == "|":
                impulses.append((next_position, "up"))
                impulses.append((next_position, "down"))

        if direction == "up":
            row, column = position
            next_row = row - 1
            if next_row < 0:
                continue

            next_position = (next_row, column)
            if next_position not in light_map:
                light_map[next_position] = ["up"]
            else:
                directions = light_map[next_position]
                if "up" not in directions:
                    directions.append("up")
                else:
                    continue

            next_tile = grid[next_row][column]
            if next_tile in ["|", "."]:
                impulses.append((next_position, direction))
            elif next_tile == "/":
                impulses.append((next_position, "right"))
            elif next_tile == "\\":
                impulses.append((next_position, "left"))
            elif next_tile == "-":
                impulses.append((next_position, "right"))
                impulses.append((next_position, "left"))

        if direction == "down":
            row, column = position
            next_row = row + 1
            if next_row >= len(grid):
                continue

            next_position = (next_row, column)
            if next_position not in light_map:
                light_map[next_position] = ["down"]
            else:
                directions = light_map[next_position]
                if "down" not in directions:
                    directions.append("down")
                else:
                    continue

            next_tile = grid[next_row][column]
            if next_tile in ["|", "."]:
                impulses.append((next_position, direction))
            elif next_tile == "/":
                impulses.append((next_position, "left"))
            elif next_tile == "\\":
                impulses.append((next_position, "right"))
            elif next_tile == "-":
                impulses.append((next_position, "right"))
                impulses.append((next_position, "left"))


def part_one(input):
    start = (0, -1)
    total = calculate_energized(input, start, "right")
    print(total)


def calculate_energized(input, start, direction):
    light_map = dict()
    move_light(input, [(start, direction)], light_map)
    total = 0
    for position, directions in light_map.items():
        if len(directions) >= 1:
            total += 1
    return total


def part_two(input):
    max = 0
    for i in range(len(input)):
        start = (i, -1)
        total = calculate_energized(input, start, "right")
        if total > max:
            max = total

        start = (i, len(input[i]))
        total = calculate_energized(input, start, "left")
        if total > max:
            max = total

    for i in range(len(input[0])):
        start = (-1, i)
        total = calculate_energized(input, start, "down")
        if total > max:
            max = total

        start = (len(input), i)
        total = calculate_energized(input, start, "up")
        if total > max:
            max = total

    print(max)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
