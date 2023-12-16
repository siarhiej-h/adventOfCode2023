from functools import cache
from re import match


def parse_input():
    input_file = "input.txt"
    rows = []
    with open(input_file) as f:
        for line in f:
            parts = line.split(" ")
            chars = parts[0]
            numbers = tuple(int(part) for part in parts[1].split(","))
            rows.append((chars, numbers))

    return rows


@cache
def get_number_of_possible_permutations(chars, numbers):
    chars = chars.strip(".")
    if chars == "":
        return 0 if numbers else 1

    if not numbers:
        return all(char != "#" for char in chars)

    if chars.startswith("?"):
        count_with_hash = get_number_of_possible_permutations('#' + chars[1:], numbers)
        count_with_dot = get_number_of_possible_permutations(chars[1:], numbers)
        return count_with_hash + count_with_dot

    expected_damaged_segment = chars[:numbers[0]]
    if len(expected_damaged_segment) < numbers[0] or "." in expected_damaged_segment:
        return 0
    if len(chars) == numbers[0]:
        return 1 if len(numbers) == 1 else 0
    if chars[numbers[0]] == "#":
        return 0

    return get_number_of_possible_permutations(chars[numbers[0] + 1:], numbers[1:])


def part_one(input):
    total = sum(get_number_of_possible_permutations(chars, numbers) for chars, numbers in input)
    print(total)


def part_two(input):
    input = [[(chars + '?') * 4 + chars, numbers * 5] for chars, numbers in input]
    total = sum(get_number_of_possible_permutations(chars, numbers) for chars, numbers in input)
    print(total)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
