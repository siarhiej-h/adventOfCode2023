from sympy import Symbol, solve_poly_system


def parse_input():
    input_file = "input.txt"
    hails = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            parts = line.split(" @ ")
            position = [int(p) for p in parts[0].split(", ")]
            speed = [int(p) for p in parts[1].split(", ")]
            hails.append((position, speed))

    return hails


def part_one(input):
    min_value = 200000000000000
    max_value = 400000000000000
    total = 0
    for i in range(len(input)):
        x11, y11, z11 = input[i][0]
        vx1, vy1, vz1 = input[i][1]

        # coordinates of the hail after one nanosecond
        x12 = x11 + vx1
        y12 = y11 + vy1
        for j in range(i + 1, len(input)):
            x21, y21, z21 = input[j][0]
            vx2, vy2, vz2 = input[j][1]
            x22 = x21 + vx2
            y22 = y21 + vy2

            intersection = get_intersection_of_two_lines((x11, y11, x12, y12), (x21, y21, x22, y22))
            if intersection is None:
                continue
            x, y = intersection
            time0 = (x - x11) / vx1
            if time0 < 0:
                continue
            time1 = (x - x21) / vx2
            if time1 < 0:
                continue
            if x < min_value or y < min_value:
                continue
            if x > max_value or y > max_value:
                continue
            total += 1
    print(total)


def get_intersection_of_two_lines(line_one_coords, line_two_coords):
    x11, y11, x12, y12 = line_one_coords
    x21, y21, x22, y22 = line_two_coords

    # y = a * x + b
    # y11 = a1 * x11 + b1
    # b1 = y11 - a1 * x11
    # y12 = a1 * x12 + b1
    # y12 = a1 * x12 + y11 - a1 * x11
    # y12 - y11 = a1 * (x12 - x11)
    # a1 = (y12 - y11) / (x12 - x11)
    # b1 = y11 - a1 * x11
    a1 = (y12 - y11) / (x12 - x11)
    a2 = (y22 - y21) / (x22 - x21)
    b1 = y11 - a1 * x11
    b2 = y21 - a2 * x21
    if a1 == a2:
        # parallel lines
        return None

    # a1 * x + b1 = a2 * x + b2
    # a1 * x - a2 * x = b2 - b1
    # (a1 - a2) * x = b2 - b1
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    return x, y


def part_two(input):
    three_hails = input[:3]
    x11, y11, z11 = three_hails[0][0]
    vx1, vy1, vz1 = three_hails[0][1]
    x21, y21, z21 = three_hails[1][0]
    vx2, vy2, vz2 = three_hails[1][1]
    x31, y31, z31 = three_hails[2][0]
    vx3, vy3, vz3 = three_hails[2][1]

#     x = x1 + vx * t
#     y = y1 + vy * t
#     z = z1 + vz * t

#     rock x: xr1 + vxr * t
#     rock y: yr1 + vyr * t
#     rock z: zr1 + vzr * t
    xr1 = Symbol('xr1')
    yr1 = Symbol('yr1')
    zr1 = Symbol('zr1')
    vxr = Symbol('vxr')
    vyr = Symbol('vyr')
    vzr = Symbol('vzr')

#     xr1 + vxr * t1 = x11 + vx1 * t1
#     yr1 + vyr * t1 = y11 + vy1 * t1
#     zr1 + vzr * t1 = z11 + vz1 * t1

    t1 = Symbol('t1')
    expr1 = xr1 + vxr * t1 - x11 - vx1 * t1
    expr2 = yr1 + vyr * t1 - y11 - vy1 * t1
    expr3 = zr1 + vzr * t1 - z11 - vz1 * t1

#     xr1 + vxr * t2 = x21 + vx2 * t2
#     yr1 + vyr * t2 = y21 + vy2 * t2
#     zr1 + vzr * t2 = z21 + vz2 * t2

    t2 = Symbol('t2')
    expr4 = xr1 + vxr * t2 - x21 - vx2 * t2
    expr5 = yr1 + vyr * t2 - y21 - vy2 * t2
    expr6 = zr1 + vzr * t2 - z21 - vz2 * t2

#     xr1 + vxr * t3 = x31 + vx3 * t3
#     yr1 + vyr * t3 = y31 + vy3 * t3
#     zr1 + vzr * t3 = z31 + vz3 * t3

    t3 = Symbol('t3')
    expr7 = xr1 + vxr * t3 - x31 - vx3 * t3
    expr8 = yr1 + vyr * t3 - y31 - vy3 * t3
    expr9 = zr1 + vzr * t3 - z31 - vz3 * t3

    equations = [expr1, expr2, expr3, expr4, expr5, expr6, expr7, expr8, expr9]
    variables = [xr1, yr1, zr1, vxr, vyr, vzr, t1, t2, t3]
    solution = solve_poly_system(equations, variables)[0]
    xr1 = solution[0]
    yr1 = solution[1]
    zr1 = solution[2]
    print(xr1 + yr1 + zr1)


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
