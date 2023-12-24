# iterate by col reversed, keep track of rock count, and kepe track of load col, get res

with open("input2") as file:
    rows = []
    for line in file.readlines():
        rows.append(list(line.strip()))
    
    rev_cols = []
    for col_i in range(len(rows[0])):
        rev_cols.append([])
        for row in reversed(rows):
            rev_cols[col_i].append(row[col_i])

    res = 0 
    for col in rev_cols:
        depth = 1
        curr_rocks = 0

        for i, elem in enumerate(col):
            if elem == "O":
                curr_rocks += 1
            if elem == "#" or i == len(col) - 1:
                # such spaghetti code lol
                if curr_rocks > 0:
                    calc_depth = depth
                    if elem == "#":
                        calc_depth -= 1

                    res += (curr_rocks * calc_depth) - int((((curr_rocks-1) * ((curr_rocks-1) + 1)) / 2))
                    curr_rocks = 0

            depth += 1
    
    print(res)