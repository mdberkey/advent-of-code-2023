
with open("input2") as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines]

    res = 0
    for line in lines:
        _, nums = line.split(":")
        nums = nums.split("|")
        target, vals = set(nums[0].split()), set(nums[1].split())
        win_val = len(target.intersection(vals)) - 1
        if win_val > -1:
            res += 2 ** win_val
    
    print(res)