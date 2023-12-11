
with open("input2") as file:
    # expand universe
    uni = []
    row_exps = []
    for i, line in enumerate(file.readlines()):
        line = list(line.strip())
        uni.append(line)
        if all(elem == '.' for elem in line):
            row_exps.append(i)
        #print(line)

    col_exps = [] 
    for j in range(len(uni[0])):
        col = []
        for i in range(len(uni)):
            col.append(uni[i][j])
        if all(elem == '.' for elem in col):
            col_exps.append(j)

    # val = 0
    # for r in row_exps:
    #     exp_row = ['.' for _ in range(len(uni[0]))]
    #     uni.insert(r + val, exp_row)
    #     val += 1
    
    # val = 0
    # for c in col_exps:
    #     for i in range(len(uni)):
    #         uni[i].insert(c + val, '.')
    #     val += 1
    
    #for r in uni:
    #    print(r)
    # get galaxies
    galaxies = []
    for i in range(len(uni)):
        for j in range(len(uni[0])):
            if uni[i][j] == "#":
                galaxies.append((i, j))
    
    # find shortest path between each (calc)
    path_sum = 0
    def get_empty_count(start, end):
        empty_rows = 0
        empty_cols = 0
        for r in row_exps:
            if start[0] > r > end[0] or start[0] < r < end[0]:
                empty_rows += 1
        for c in col_exps:
            if start[1] > c > end[1] or start[1] < c < end[1]:
                empty_cols += 1 
        return empty_cols + empty_rows

    from itertools import combinations

    for start, end in combinations(galaxies, 2):
        row_dist = abs(start[0] - end[0])
        col_dist = abs(start[1] - end[1])
        expanse_dist = get_empty_count(start, end)
        expanse_dist_calc = (expanse_dist * 1000000) - expanse_dist
        path_sum += row_dist + col_dist + expanse_dist_calc

    print(path_sum)
