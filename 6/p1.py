
with open("input1") as f:
    lines = [line.strip() for line in f.readlines()]
    times = [int(val) for val in lines[0].split()[1:]]
    dists = [int(val) for val in lines[1].split()[1:]]

    ways_list = []
    # BF: iterate over all possible distances
    for t, d in zip(times, dists):
        ways = 0
        for i in range(t+1):
            curr_d = i * (t - i)
            if curr_d > d:
                ways += 1
        if ways > 0:
            ways_list.append(ways)
    
    res = 1
    for ways in ways_list:
        res *= ways
    print(res)
