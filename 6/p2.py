
with open("input1") as f:
    lines = [line.strip() for line in f.readlines()]
    time = int("".join(lines[0].split()[1:]))
    dist = int("".join(lines[1].split()[1:]))

    # BF: iterate over all possible distances
    res = 0
    for i in range(time+1):
        curr_d = i * (time - i)
        if curr_d > dist:
            res += 1
    
    print(res)