def part_one(input):
    line_one, line_two = input
    times = line_one.split()[1:]
    distances = line_two.split()[1:]

    data = dict()
    for i in range(len(times)):
        data[int(times[i])] = int(distances[i])

    res = 1
    for time, top_distance in data.items():
        attempts = 0
        for charge_time in range(1, time):
            distance = (time - charge_time) * charge_time
            if distance > top_distance:
                attempts += 1
        res *= attempts
    print(res)


def part_two(input):
    line_one, line_two = input
    times = line_one.replace(" ", "").split(":")[1:]
    distances = line_two.replace(" ", "").split(":")[1:]
    data = dict()
    for i in range(len(times)):
        data[int(times[i])] = int(distances[i])

    res = 1
    for time, top_distance in data.items():
        attempts = 0
        for charge_time in range(1, time):
            distance = (time - charge_time) * charge_time
            if distance > top_distance:
                attempts += 1
        res *= attempts
    print(res)


def parse_input():
    input_file = "input.txt"
    with open(input_file) as f:
        line_one = f.readline().strip()
        line_two = f.readline().strip()
        return line_one, line_two


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
