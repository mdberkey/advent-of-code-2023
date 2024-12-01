
def calc_hash(string):
    res = 0
    for c in string:
        res += ord(c)
        res *= 17
        res %= 256
    return res

with open("input") as file:
    
    steps = file.read().strip().split(",")
    labels = []
    operations = []
    for step in steps:
        if "-" in step:
            label = step.split("-")[0]
            labels.append(label)
            operations.append("-")
        else:
            label, op = step.split("=")
            labels.append(label)
            operations.append(int(op))

    boxes = [{} for _ in range(256)]
    for l, op in zip(labels, operations):
        lhash = calc_hash(l)
        
        if op == "-":
            if l not in boxes[lhash]:
                continue
            boxes[lhash].pop(l)
        else:
            boxes[lhash][l] = (l, op)

    res = 0    
    for i, box in enumerate(boxes):
        curr_focus = 1 + i
        for i, (_, flen) in enumerate(box.values()):
            res += curr_focus * (1 + i) * flen
    
    print(res)
