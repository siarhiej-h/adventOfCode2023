def parse_input():
    input_file = "input.txt"
    grid = []
    with open(input_file) as f:
        for line in f:
            row = list(line.strip())
            grid.append(row)

    return grid


def part_one(input):
    sum = calculate_distance_sum(input, 1)
    print(sum)


def calculate_distance_sum(universe, expansion_rate):
    all_galaxies = [(row, column) for row in range(len(universe)) for column in range(len(universe[row])) if universe[row][column] == "#"]
    all_empty_columns = [column for column in range(len(universe[0])) if all(universe[row][column] == "." for row in range(len(universe)))]
    all_empty_rows = [row for row in range(len(universe)) if all(universe[row][column] == "." for column in range(len(universe[row])))]
    sum = 0
    for i in range(len(all_galaxies)):
        for j in range(i + 1, len(all_galaxies)):
            row1, col1 = all_galaxies[i]
            row2, col2 = all_galaxies[j]
            distance = abs(row1 - row2) + abs(col1 - col2)
            for empty_row in all_empty_rows:
                if row1 < empty_row < row2 or row2 < empty_row < row1:
                    distance += expansion_rate
            for empty_column in all_empty_columns:
                if col1 < empty_column < col2 or col2 < empty_column < col1:
                    distance += expansion_rate
            sum += distance
    return sum


def part_two(input):
    sum = calculate_distance_sum(input, 999999)
    print(sum)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
