from collections import Counter


def val_to_int(val):
    if val == "A":
        return 14
    elif val == "K":
        return 13
    elif val == "Q":
        return 12
    elif val == "J":
        return 11
    elif val == "T":
        return 10
    else:
        return int(val)

with open("input1.txt", "r") as file:
    hand_bets = {}
    for line in file.readlines():
        line = line.strip().split(" ")
        string = line[0]
        val = int(line[1])
        key = tuple([val_to_int(char) for char in string])
        hand_bets[key] = val
    
    hands = [[] for i in range(7)]
    for hand in hand_bets.keys():
        hand = [val_to_int(char) for char in hand]
        unique_vals = set(hand)
        counts = Counter(hand)

        if len(unique_vals) == 1:
            # 5 of a kind
            hands[0].append(hand)
        elif len(unique_vals) == 2:
            if 1 in counts.values():
                # 4 of a kind
                hands[1].append(hand)
            else:
                # full house
                hands[2].append(hand)
        elif len(unique_vals) == 3:
            if 3 in counts.values():
                # 3 of a kind
                hands[3].append(hand)
            else:
                # 2 pairs
                hands[4].append(hand)
        elif len(unique_vals) == 4:
            # 1 pair
            hands[5].append(hand)
        else:
            hands[6].append(hand)

    num_hands = [] 
    for li in hands:
        num_hand_li = []
        for hand in li:
            num_hand_li.append(hand)
        sorted_num_hand_li = sorted(num_hand_li, key=lambda x: (x[0], x[1], x[2], x[3], x[4]), reverse=True)
        num_hands.append(sorted_num_hand_li)
    
    # calc vals
    print(num_hands)

