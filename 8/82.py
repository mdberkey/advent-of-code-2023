from math import lcm


with open('input2.txt', 'r') as file:
    res = 0
    lines = file.readlines()
    # L = true, R = false
    instructions = [True if var == 'L' else False for var in lines[0].strip()]
    stops = {}
    for line in lines[2:]:
        line = line.strip()
        if line:
            chars = [char for char in line]
            key = tuple(chars[:3])
            tup = tuple(chars[7:10]), tuple(chars[12:15])
            stops[key] = tup
    
    curr_stops = []
    for key in stops.keys():
        if key[2] == 'A':
            curr_stops.append(key)
    print(len(curr_stops))
    
    loop_vals = {}
    count = 0
    condition = True
    while condition:
        for inst in instructions:
            new_stops = []
            for stop in curr_stops:
                if inst:
                    new_stops.append(stops[stop][0])
                else:
                    new_stops.append(stops[stop][1])
            curr_stops = new_stops
            count += 1

            for stop in curr_stops:
                if stop[2] == 'Z' and stop not in loop_vals:
                    loop_vals[stop] = count

            if len(loop_vals) == len(curr_stops):
                condition = False
                break
        #print(loop_vals.values())

    print(lcm(*loop_vals.values()))

# find values of loops
# get least common multiple