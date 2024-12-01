
def calc_hash(string):
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res %= 256
    return res

with open("input") as file:
    
    steps = file.read().strip().split(",")

    res = 0

    for step in steps:
        res += calc_hash(step)
    
    print(res)
