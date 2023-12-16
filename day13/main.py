def parse_input():
    input_file = "input.txt"
    patterns = []
    rows = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            if not line:
                patterns.append(rows)
                rows = []
                continue

            rows.append(line)
    if rows:
        patterns.append(rows)
    return patterns


def find_vertical_reflection(pattern, expected_smudges=0):
    for i in range(1, len(pattern[0])):
        reflection_size = min(i, len(pattern[0]) - i)
        smudges_found = 0
        for j in range(reflection_size):
            for row in pattern:
                is_reflection = row[i - j - 1] == row[i + j]
                if not is_reflection:
                    smudges_found += 1
        if smudges_found == expected_smudges:
            return i
    return None


def find_horizontal_reflection(pattern, expected_smudges=0):
    for i in range(1, len(pattern)):
        reflection_size = min(i, len(pattern) - i)
        smudges_found = 0
        for j in range(reflection_size):
            for col in range(len(pattern[0])):
                is_reflection = pattern[i - j - 1][col] == pattern[i + j][col]
                if not is_reflection:
                    smudges_found += 1
        if smudges_found == expected_smudges:
            return i
    return None


def part_one(input):
    result = 0
    for pattern in input:
        vertical_reflection = find_vertical_reflection(pattern)
        if vertical_reflection:
            result += vertical_reflection
        horizontal_reflection = find_horizontal_reflection(pattern)
        if horizontal_reflection:
            result += 100 * horizontal_reflection
    print(result)


def part_two(input):
    result = 0
    for pattern in input:
        vertical_reflection = find_vertical_reflection(pattern, 1)
        if vertical_reflection:
            result += vertical_reflection
        horizontal_reflection = find_horizontal_reflection(pattern, 1)
        if horizontal_reflection:
            result += 100 * horizontal_reflection
    print(result)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
