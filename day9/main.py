def part_one(input):
    total = sum((get_next_prediction(sequence) for sequence in input))
    print(total)


def part_two(input):
    total = sum((get_previous_prediction(sequence) for sequence in input))
    print(total)


def get_next_prediction(sequence):
    diff_list = []
    all_zero = True
    for i in range(1, len(sequence)):
        diff = sequence[i] - sequence[i-1]
        diff_list.append(diff)
        if diff != 0:
            all_zero = False
    if all_zero is True:
        return sequence[-1]

    return sequence[-1] + get_next_prediction(diff_list)


def get_previous_prediction(sequence):
    diff_list = []
    all_zero = True
    for i in range(0, len(sequence) - 1):
        diff = sequence[i] - sequence[i+1]
        diff_list.append(diff)
        if diff != 0:
            all_zero = False
    if all_zero is True:
        return sequence[0]

    return sequence[0] + get_previous_prediction(diff_list)


def parse_input():
    input_file = "input.txt"
    sequences = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            sequences.append([int(v) for v in line.split(" ")])

    return sequences


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
