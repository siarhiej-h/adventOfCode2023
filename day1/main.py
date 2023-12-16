# get first digit
def get_first_digit(line, digits):
    min_index = len(line)
    first_digit = None
    for digit in digits:
        index = line.find(digit)
        if index != -1 and index < min_index:
            min_index = index
            first_digit = digit

    if len(first_digit) > 1:
        first_digit = convert_digit(first_digit)

    return first_digit


def convert_digit(line):
    digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }
    return digits[line]


def get_last_digit(line, digits):
    max_index = -1
    last_digit = None
    for digit in digits:
        index = line.rfind(digit)
        if index > max_index:
            max_index = index
            last_digit = digit

    if len(last_digit) > 1:
        last_digit = convert_digit(last_digit)

    return last_digit


def part_one(lines):
    sum = 0
    input_file = "input.txt"
    with open(input_file) as f:
        for line in f.readlines():
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)
            number = int(first_digit + last_digit)
            sum += number
    print(sum)


def part_two():
    sum = 0
    input_file = "input.txt"
    digits = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine"
    ]
    with open(input_file) as f:
        for line in f.readlines():
            first_digit = get_first_digit(line, digits)
            last_digit = get_last_digit(line, digits)
            number = int(first_digit + last_digit)
            print(number)
            sum += number
    print(sum)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # part_one()
    part_two()
