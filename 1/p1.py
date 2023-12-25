
with open("input2") as f:
    lines = f.read().splitlines()
    res = 0

    for line in lines:
        if line:
            digits = [char for char in line if char.isdigit()]
            res += int(digits[0] + digits[-1])
    print(res)