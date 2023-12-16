def part_one(input):
    instructions, nodes = input

    instructions_active = instructions.copy()
    steps = 0
    directions = nodes["AAA"]
    while True:
        steps += 1
        if not instructions_active:
            instructions_active = instructions.copy()

        instruction = instructions_active.pop(0)
        if instruction == "L":
            direction = directions[0]
        else:
            direction = directions[1]

        if direction == "ZZZ":
            break

        directions = nodes[direction]

    print(steps)


def part_two(input):
    instructions, nodes = input

    instructions_active = instructions.copy()
    steps = 0
    directions_list = [v for k, v in nodes.items() if k.endswith("A")]
    print(directions_list)
    sequences = [0 for _ in range(len(directions_list))]
    while True:
        steps += 1
        if not instructions_active:
            instructions_active = instructions.copy()

        instruction = instructions_active.pop(0)

        if instruction == "L":
            direction = [v[0] for v in directions_list]
        else:
            direction = [v[1] for v in directions_list]

        for i in range(len(direction)):
            d = direction[i]
            if d.endswith("Z"):
                print(d)
                sequences[i] = steps

        if all(s > 0 for s in sequences):
            break
        if all(d.endswith("Z") for d in direction):
            break

        directions_list = [nodes[d] for d in direction]

    print(find_least_common_multiple(sequences))


def find_least_common_multiple(numbers):
    lcm = numbers[0]
    for i in numbers[1:]:
        lcm = lcm * i // find_greatest_common_divisor(lcm, i)
    return lcm


def find_greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a


def parse_input():
    input_file = "input.txt"
    nodes = dict()
    with open(input_file) as f:
        instructions = list(f.readline().strip())
        f.readline()
        for line in f:
            line = line.strip()
            parts = line.split(" = ")
            key = parts[0]
            directions = parts[1][1:-1].split(", ")
            nodes[key] = directions

    print(nodes)
    return instructions, nodes


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
