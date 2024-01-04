# store inputs into lists of list of range tuples
# iterate over range lists and convert numbers to new range tuples
# return min res

with open("input1") as f:
    lines = [line.strip() for line in f.readlines()]
    seeds = [int(val) for val in lines[0].split(":")[1].split()]
    # last num is exclusive
    seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

    num_lines = []
    for line in lines[1:]:
        if not line:
            num_lines.append([])
            continue
        elif not line[0].isdigit():
            continue
        num_lines[-1].append(tuple(int(val) for val in line.split()))
    
    print(seed_ranges)
    print(num_lines)

    # iterate num maps, iterate seed ranges, iterate map ranges, convert to group of new ranges, append to new ranges, continue, return min

    for num_map in num_lines:
        for seed_range in seed_ranges:
            curr_ranges = [seed_range]
            new_ranges = []

            for (map_dest, map_src, map_len) in num_map:
                for i, (seed_src, seed_len) in enumerate(curr_ranges):
                    seed_end = seed_src + seed_len - 1 # inclusive vals
                    map_end = map_src + map_len - 1 # inclusive val


                    if seed_end < map_src or seed_src > map_end:
                        # outside map
                        new_ranges.append((seed_src, seed_len))
                    elif seed_src >= map_src and seed_end <= map_end:
                        # inside map
                        new_ranges.append((map_dest, seed_len))
                    elif seed_src < map_src and seed_end > map_end:
                        # engulfs map
                        left = (seed_src, map_src - seed_src)
                        mid = (map_dest, map_len)
                        right = (map_end + 1, seed_len - (map_end - seed_src))
                        new_ranges.extend([left, mid, right])
                    elif seed_src < map_src:
                        # left side overlap
                        left = (seed_src, seed_len - (seed_end - map_src))
                        right = (map_dest, seed_len - (map_src - seed_src))
                        new_ranges.extend([left, right])
                    else:
                        # right side overlap
                        left = (map_dest, seed_len - (seed_end - map_end))
                        right = (seed_end, map_len - (seed_end - map_src))
                        new_ranges.extend([left, right])
                    
                    print(new_ranges)
                    exit()
 