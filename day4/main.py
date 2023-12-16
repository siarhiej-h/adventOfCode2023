def part_one(input):
    sum = 0
    for card_number, winning, player_cards in input:
        result = 0
        for card in player_cards:
            if card in winning:
                if result == 0:
                    result = 1
                else:
                    result *= 2
        sum += result
    print(sum)


def part_two(input):
    card_counts = dict()
    cards_total = 0
    for card_number, winning, player_cards in input:
        matches = 0
        for card in player_cards:
            if card in winning:
                matches += 1
        iterations = 1
        if card_number in card_counts:
            iterations = card_counts[card_number]
        for number in range(card_number + 1, card_number + 1 + matches):
            if number not in card_counts:
                card_counts[number] = 1
            card_counts[number] += iterations
        cards_total += iterations
    print(cards_total)

def parse_input():
    input_file = "input.txt"
    with open(input_file) as f:
        for line in f.readlines():
            line = line.strip().replace("Card ", "")
            line = line.replace("  ", " ")
            parts = line.split(": ")
            card_number = int(parts[0])
            cards = parts[1].split("|")
            winning = {int(value) for value in cards[0].strip().split(" ")}
            player_cards = [int(value) for value in cards[1].strip().split(" ")]
            yield card_number, winning, player_cards


if __name__ == '__main__':
    input = parse_input()
    # part_one(input)
    # part_two(input)
