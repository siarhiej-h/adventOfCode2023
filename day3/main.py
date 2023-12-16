import re

def part_one(input):
    numbers = []
    for row in range(len(input)):
        start = None
        end = None
        for col in range(len(input[row])):
            is_digit = input[row][col].isdigit()
            if is_digit:
                end = col
                if start is None:
                    start = col
            if not is_digit or col == len(input[row]) - 1:
                if start is not None:
                    has_symbols, indices = has_adjacent_symbols(input, row, start, end, is_symbol_p1)
                    if has_symbols:
                        numbers.append(int(''.join(input[row][start:end + 1])))
                    start = None
                    end = None
    print(sum(numbers))



def part_two(input):
    numbers = dict()
    for row in range(len(input)):
        start = None
        end = None
        for col in range(len(input[row])):
            is_digit = input[row][col].isdigit()
            if is_digit:
                end = col
                if start is None:
                    start = col
            if not is_digit or col == len(input[row]) - 1:
                if start is not None:
                    has_adjacent, indices = has_adjacent_symbols(input, row, start, end, is_symbol_p2)
                    number = int(''.join(input[row][start:end + 1]))
                    if has_adjacent is True:
                        for index in indices:
                            if index not in numbers:
                                numbers[index] = []
                            numbers[index].append(number)
                    start = None
                    end = None
    print(numbers)
    gears_sum = sum((values[0] * values[1] for i, values in numbers.items() if len(values) == 2))
    print(gears_sum)


def is_symbol_p1(character):
    return character.isdigit() is False and character != '.'


def is_symbol_p2(character):
    return character == '*'


def has_adjacent_symbols(schematic, row, col_start, col_end, is_symbol):
    indices = []
    row_length = len(schematic[0])
    if row > 0:
        for col in range(col_start, col_end + 1):
            character = schematic[row - 1][col]
            if is_symbol(character):
                indices.append((row - 1) * row_length + col)
        if col_start > 0:
            character = schematic[row - 1][col_start - 1]
            if is_symbol(character):
                indices.append((row - 1) * row_length + (col_start - 1))
        if col_end < len(schematic[row]) - 1:
            character = schematic[row - 1][col_end + 1]
            if is_symbol(character):
                indices.append((row - 1) * row_length + (col_end + 1))
    if row < len(schematic) - 1:
        for col in range(col_start, col_end + 1):
            character = schematic[row + 1][col]
            if is_symbol(character):
                indices.append((row + 1) * row_length + col)
        if col_start > 0:
            character = schematic[row + 1][col_start - 1]
            if is_symbol(character):
                indices.append((row + 1) * row_length + (col_start - 1))
        if col_end < len(schematic[row]) - 1:
            character = schematic[row + 1][col_end + 1]
            if is_symbol(character):
                indices.append((row + 1) * row_length + (col_end + 1))
    if col_start > 0:
        character = schematic[row][col_start - 1]
        if is_symbol(character):
            indices.append(row * row_length + (col_start - 1))
    if col_end < len(schematic[row]) - 1:
        character = schematic[row][col_end + 1]
        if is_symbol(character):
            indices.append(row * row_length + (col_end + 1))

    return True if indices else False, indices


def parse_input():
    input_file = "input.txt"
    schematic = []
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip()
            row = []
            for ch in line:
                row.append(ch)
            schematic.append(row)
    return schematic


if __name__ == '__main__':
    input = parse_input()
    print(input)
    part_one(input)
    part_two(input)
