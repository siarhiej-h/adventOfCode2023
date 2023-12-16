def is_valid_game(cubes_total, game_round):
    if game_round["red"] > cubes_total["red"]:
        return False
    if game_round["blue"] > cubes_total["blue"]:
        return False
    if game_round["green"] > cubes_total["green"]:
        return False
    return True


def part_one():
    input_file = "input.txt"
    valid_games = set()
    cubes_total = {
        "green": 13,
        "red": 12,
        "blue": 14
    }
    with open(input_file) as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            parts = line.split(": ")
            game_info = parts[0].split(" ")
            game_id = int(game_info[1])
            rounds = parts[1].split("; ")
            is_valid = True
            for game_round in rounds:
                game = dict(red=0, green=0, blue=0)
                cubes = game_round.split(", ")
                for cube in cubes:
                    cube_parts = cube.split(" ")
                    number = int(cube_parts[0])
                    color = cube_parts[1]
                    game[color] += number

                if not is_valid_game(cubes_total, game):
                    is_valid = False
                    break

            if is_valid:
                valid_games.add(game_id)

    print(valid_games)
    print(sum(valid_games))


def part_two():
    input_file = "input.txt"
    sum = 0
    with open(input_file) as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            parts = line.split(": ")
            rounds = parts[1].split("; ")
            color_minimums = dict(red=0, green=0, blue=0)
            for game_round in rounds:
                cubes = game_round.split(", ")
                for cube in cubes:
                    cube_parts = cube.split(" ")
                    number = int(cube_parts[0])
                    color = cube_parts[1]
                    if color_minimums[color] < number:
                        color_minimums[color] = number
            power = color_minimums["green"] * color_minimums["red"] * color_minimums["blue"]
            sum += power
    print(sum)


if __name__ == '__main__':
    # part_one()
    part_two()
    pass
