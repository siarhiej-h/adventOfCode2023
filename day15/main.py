def parse_input():
    input_file = "input.txt"
    with open(input_file) as f:
        line = f.readline()
        return line.split(",")


def get_command_hash(command):
    start = 0
    for char in command:
        start += ord(char)
        start *= 17
        start = start % 256
    return start


def part_one(input):
    total = sum(get_command_hash(command) for command in input)
    print(total)


def remove_lens_from_box(box, lens):
    for i in range(len(box)):
        if box[i][0] == lens:
            box.pop(i)
            return


def add_lens_to_box(box, lens, value):
    for i in range(len(box)):
        if box[i][0] == lens:
            box[i] = (lens, value)
            return

    box.append((lens, value))


def part_two(input):
    boxes = [[] for _ in range(256)]
    for full_command in input:
        if "=" in full_command:
            lens, value = full_command.split("=")
            box_hash = get_command_hash(lens)
            box = boxes[box_hash]
            value = int(value)
            add_lens_to_box(box, lens, value)

        elif "-" in full_command:
            lens = full_command[:-1]
            box_hash = get_command_hash(lens)
            box = boxes[box_hash]
            remove_lens_from_box(box, lens)

    total = 0
    for i in range(len(boxes)):
        box = boxes[i]
        if not box:
            continue
        factor_1 = i + 1
        for j in range(len(box)):
            factor_2 = j + 1
            factor_3 = box[j][1]
            total += factor_1 * factor_2 * factor_3
    print(total)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
