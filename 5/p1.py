# store inputs into lists of list of range tuples
# iterate over range lists and convert numbers to mapped res
# return min res

with open("input2") as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = [int(val) for val in lines[0].split(":")[1].split()]

    num_lines = []
    for line in lines[1:]:
        if not line:
            num_lines.append([])
            continue
        elif not line[0].isdigit():
            continue
        num_lines[-1].append(tuple(int(val) for val in line.split()))

    res = seeds
    for num_map in num_lines:
        for i, val in enumerate(res):
            curr_val = None
            for (dest, src, length) in num_map:
                if val >= src and val < src + length:
                    curr_val = dest + val - src
                    break

            if not curr_val:
                curr_val = val
            
            res[i] = curr_val
    
    print(min(res))
            