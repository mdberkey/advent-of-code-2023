
with open("input2") as f:
    cube_counts = {'red': 12, 'green': 13, 'blue': 14}    
    lines = f.readlines()
    invalid_games = set()
    game_ids = set()

    for line in lines:
        valid = True
        game_id, counts = line.split(':')
        game_id = int(game_id.split()[1])
        game_ids.add(game_id)

        sets = counts.split(';')
        for cset in sets:
            cset.strip().split(',')
            vals = cset.strip().split(',')

            for val in vals:
                num, color = val.split()
                if cube_counts[color] < int(num):
                    valid = False
                    invalid_games.add(game_id)
                    break
    
    valid_games = game_ids.symmetric_difference(invalid_games)
    res = sum(valid_games)
    
    print(res)


