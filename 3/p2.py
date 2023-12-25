
with open("input2") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]
    values = []

    for i in range(len(lines)):
        values.append([])
        for j in range(len(lines[0])):
            values[i].append(lines[i][j])
    
    num_tuples = set()
    for row_i, line in enumerate(values):
        i = 0

        while i < len(line):
            str_num = ""
            start_i = i

            while i < len(line) and line[i].isdigit():
                str_num = str_num + line[i]
                i += 1
            end_i = i

            if str_num != "":
                num_tuples.add((row_i, start_i, end_i, int(str_num)))
            i += 1

    res = 0
    for i in range(len(values)):
        for j in range(len(values[0])):
            symbol = values[i][j]
            if symbol == "*":
                valid_tuples = set()
                for tup in num_tuples:
                    if i - 1 <= tup[0] <= i + 1 and tup[1] - 1 <= j < tup[2] + 1:
                        valid_tuples.add(tup)
                if len(valid_tuples) == 2:
                    gear_ratio = 1
                    for tup in valid_tuples:
                        gear_ratio *= tup[3]
                    res += gear_ratio
                num_tuples = num_tuples - valid_tuples
    print(res)