
with open("input2") as f:
    lines = f.readlines()
    res = 0

    for line in lines:
        min_counts = {'red': 0, 'green': 0, 'blue': 0}    
        _, counts = line.split(':')
        sets = counts.split(';')

        for cset in sets:
            cset.strip().split(',')
            vals = cset.strip().split(',')

            for val in vals:
                num, color = val.split()

                if min_counts[color] < int(num):
                    min_counts[color] = int(num)
        
        power = 1
        for val in min_counts.values():
            power *= val
        res += power
    
    print(res)
