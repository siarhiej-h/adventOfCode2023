def parse_input():
    input_file = "input.txt"
    grid = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            parts = line.split(" ")
            direction = parts[0]
            length = int(parts[1])
            hex_value = parts[2][1:-1]
            grid.append((direction, length, hex_value))
    return grid


def calculate_area(points):
    area = 0
    for i in range(-1, len(points) - 1):
        area += points[i][1] * (points[i + 1][0] - points[i - 1][0])
    area //= 2
    return area


def calculate_interior(area, boundary):
    return int(area - boundary // 2 + 1)


def part_one(input):
    point = (0, 0)
    points = [point]
    boundary = 0
    for direction, length, _ in input:
        if direction == "R":
            point = (point[0], point[1] + length)
        elif direction == "L":
            point = (point[0], point[1] - length)
        elif direction == "U":
            point = (point[0] - length, point[1])
        elif direction == "D":
            point = (point[0] + length, point[1])
        points.append(point)
        boundary += length

    area = calculate_area(points)
    interior = calculate_interior(area, boundary)
    print(interior + boundary)


def hex_to_dec(hex_value):
    return int(hex_value, 16)


def part_two(input):
    new_input = []
    for _, _, hex_value in input:
        direction = convert_direction(int(hex_value[-1]))
        length = hex_to_dec(hex_value[1:-1])
        new_input.append((direction, length, None))
    part_one(new_input)


def convert_direction(numeric_value):
    if numeric_value == 0:
        return "R"
    if numeric_value == 1:
        return "D"
    if numeric_value == 2:
        return "L"
    if numeric_value == 3:
        return "U"


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
