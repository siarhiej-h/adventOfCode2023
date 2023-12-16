from functools import cmp_to_key


def part_one(input):
    rank = 1
    sum = 0
    for (hand, bid) in sorted(input, key=cmp_to_key(compare_hands)):
        sum += bid * rank
        rank += 1

    print(sum)


def compare_hands(left, right):
    hand1, _ = left
    hand2, _ = right
    hand1_type = get_hand_type(hand1)
    hand2_type = get_hand_type(hand2)

    if hand1_type < hand2_type:
        return 1
    elif hand1_type > hand2_type:
        return -1
    else:
        for i in range(len(hand1)):
            card1 = hand1[i]
            card2 = hand2[i]
            if card1 == card2:
                continue
            if card1 == "A":
                return 1
            if card2 == "A":
                return -1
            if card1 == "K":
                return 1
            if card2 == "K":
                return -1
            if card1 == "Q":
                return 1
            if card2 == "Q":
                return -1
            if card1 == "J":
                return 1
            if card2 == "J":
                return -1
            if card1 == "T":
                return 1
            if card2 == "T":
                return -1
            if int(card1) > int(card2):
                return 1
            return -1


def part_two(input):
    rank = 1
    sum = 0
    for (hand, bid) in sorted(input, key=cmp_to_key(compare_hands_p2)):
        sum += bid * rank
        rank += 1

    print(sum)


def get_hand_type_p2(hand):
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    j_count = counts.pop("J", 0)
    if j_count == 5:
        return 1

    if j_count > 0:
        max_count = max(counts.values())
        for card in counts:
            if counts[card] == max_count:
                counts[card] += j_count
                break

    if len(counts) == 1:
        return 1

    if len(counts) == 2:
        if 4 in counts.values():
            return 2
        return 3

    if len(counts) == 3:
        if 3 in counts.values():
            return 4
        return 5

    if len(counts) == 4:
        return 6

    return 7


def compare_hands_p2(left, right):
    hand1, _ = left
    hand2, _ = right
    hand1_type = get_hand_type_p2(hand1)
    hand2_type = get_hand_type_p2(hand2)

    if hand1_type < hand2_type:
        return 1
    elif hand1_type > hand2_type:
        return -1
    else:
        for i in range(len(hand1)):
            card1 = hand1[i]
            card2 = hand2[i]
            if card1 == card2:
                continue
            if card1 == "J":
                return -1
            if card2 == "J":
                return 1
            if card1 == "A":
                return 1
            if card2 == "A":
                return -1
            if card1 == "K":
                return 1
            if card2 == "K":
                return -1
            if card1 == "Q":
                return 1
            if card2 == "Q":
                return -1
            if card1 == "T":
                return 1
            if card2 == "T":
                return -1
            if int(card1) > int(card2):
                return 1
            return -1


def get_hand_type(hand):
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    if len(counts) == 1:
        return 1

    if len(counts) == 2:
        if 4 in counts.values():
            return 2
        return 3

    if len(counts) == 3:
        if 3 in counts.values():
            return 4
        return 5

    if len(counts) == 4:
        return 6

    return 7


def parse_input():
    input_file = "input.txt"
    games = []
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            parts = line.split(" ")
            hands = list(parts[0])
            bid = int(parts[1])
            games.append((hands, bid))
    return games


if __name__ == "__main__":
    input = parse_input()
    part_one(input)
    part_two(input)
