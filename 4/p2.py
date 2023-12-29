
with open("input2") as f:
    lines = [x.strip() for x in f.readlines()]
    
    res = 0
    card_vals = {}
    for line in lines:
        game_id, nums = line.split(":")
        game_id = int(game_id.split()[1])
        nums = nums.split("|")
        target, vals = set(nums[0].split()), set(nums[1].split())
        win_vals = target.intersection(vals)

        if game_id not in card_vals:
            card_vals[game_id] = 0
        card_vals[game_id] += 1

        for win_val in range(game_id + 1, game_id + len(win_vals) + 1):
            if win_val not in card_vals:
                card_vals[win_val] = 0
            card_vals[win_val] += card_vals[game_id]
    
    for val in card_vals.values():
        res += val
    
    print(res)