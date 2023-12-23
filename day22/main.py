from collections import deque
from collections import defaultdict
from copy import deepcopy


def parse_input():
    input_file = "input.txt"
    bricks = []
    with open(input_file) as f:
        index = -1
        for line in f:
            index += 1
            line = line.strip()
            start, end = line.split("~")
            start = [int(coord) for coord in start.split(",")]
            end = [int(coord) for coord in end.split(",")]

            if start[0] > end[0]:
                x_range = (end[0], start[0])
            else:
                x_range = (start[0], end[0])

            if start[1] > end[1]:
                y_range = (end[1], start[1])
            else:
                y_range = (start[1], end[1])

            if start[2] > end[2]:
                z_range = (end[2], start[2])
            else:
                z_range = (start[2], end[2])

            bricks.append([x_range, y_range, z_range, index])

    return bricks


def part_one(input):
    bricks = input
    bricks = move(bricks)

    supported_by = defaultdict(list)
    by_min_z = defaultdict(list)
    by_max_z = defaultdict(list)
    for i in range(len(bricks)):
        brick = bricks[i]
        by_min_z[brick[2][0]].append(i)
        by_max_z[brick[2][1]].append(i)

    for key in sorted(by_max_z.keys()):
        layer_bricks = by_max_z[key]
        possibly_supported = by_min_z.get(key + 1, [])
        for brick_index in layer_bricks:
            brick = bricks[brick_index]
            for other_brick_index in possibly_supported:
                other_brick = bricks[other_brick_index]
                if is_overlap(brick, other_brick):
                    supported_by[other_brick_index].append(brick_index)

    irremovable = set()
    for i in range(len(bricks)):
        if i in supported_by:
            supporters = supported_by[i]
            if len(supporters) == 1:
                irremovable.add(supporters[0])

    print(len(bricks) - len(irremovable))


def move(bricks):
    bricks = sorted(bricks, key=lambda x: x[2][0])
    bricks_below = deque()
    for brick in bricks:
        for brick_below in reversed(bricks_below):
            if is_overlap(brick, brick_below):
                next_z0 = brick_below[2][1] + 1
                offset = next_z0 - brick[2][0]
                brick[2] = (brick[2][0] + offset, brick[2][1] + offset)
                index = len(bricks_below)
                for bb in reversed(bricks_below):
                    if brick[2][1] > bb[2][1]:
                        break
                    index -= 1
                bricks_below.insert(index, brick)
                break
        else:
            offset = 1 - brick[2][0]
            brick[2] = (brick[2][0] + offset, brick[2][1] + offset)
            bricks_below.appendleft(brick)
            continue
    return list(bricks_below)


def is_overlap(brick1, brick2):
    b1_x0, b1_x1 = brick1[0]
    b1_y0, b1_y1 = brick1[1]
    b2_x0, b2_x1 = brick2[0]
    b2_y0, b2_y1 = brick2[1]

    if b1_x0 > b2_x1 or b1_x1 < b2_x0:
        return False
    if b1_y0 > b2_y1 or b1_y1 < b2_y0:
        return False
    return True


def part_two(input):
    bricks = input
    bricks = move(bricks)

    supports = defaultdict(list)
    supported_by = defaultdict(list)
    by_min_z = defaultdict(list)
    by_max_z = defaultdict(list)
    for i in range(len(bricks)):
        brick = bricks[i]
        by_min_z[brick[2][0]].append(i)
        by_max_z[brick[2][1]].append(i)

    for key in sorted(by_max_z.keys()):
        layer_bricks = by_max_z[key]
        possibly_supported = by_min_z.get(key + 1, [])
        for brick_index in layer_bricks:
            brick = bricks[brick_index]
            for other_brick_index in possibly_supported:
                other_brick = bricks[other_brick_index]
                if is_overlap(brick, other_brick):
                    supports[brick_index].append(other_brick_index)
                    supported_by[other_brick_index].append(brick_index)

    irremovable = set()
    for i in range(len(bricks)):
        if i in supported_by:
            supporters = supported_by[i]
            if len(supporters) == 1:
                irremovable.add(supporters[0])

    sum_fallen = 0

    for i in irremovable:
        supports_temp = deepcopy(supports)
        supported_by_temp = deepcopy(supported_by)

        total = 0
        removed = get_disruptions(supports_temp, supported_by_temp, [i])
        while removed:
            total += len(removed)
            removed = get_disruptions(supports_temp, supported_by_temp, removed.copy())

        sum_fallen += total

    print(sum_fallen)


def get_disruptions(supports, supported_by, removed_bricks):
    removed = set()
    for i in removed_bricks:
        supported_by.pop(i, None)
        supported = supports.pop(i, [])
        for supported_brick in supported:
            if len(supported_by[supported_brick]) == 1:
                removed.add(supported_brick)
            else:
                supported_by[supported_brick].remove(i)
    return removed


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
