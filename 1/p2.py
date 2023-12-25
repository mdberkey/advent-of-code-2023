
with open("input2") as f:
    digit_strs = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
    digit_dict = {digit_strs[i]: i for i in range(10)}
    rev_digit_strs = tuple([string[::-1] for string in digit_strs])
    rev_digit_dict = {rev_digit_strs[i]: i for i in range(10)}

    lines = f.read().splitlines()
    res = 0

    for line in lines:
        first_digit = None
        for i, char in enumerate(line):
            for digit_str in digit_strs:
                if str(line[i:]).startswith(digit_str):
                    first_digit = digit_dict[digit_str]
                    break
            
            if first_digit != None:
                break
            
            if char.isdigit():
                first_digit = int(char)
                break
        
        second_digit = None
        line = line[::-1]
        for i, char in enumerate(line):
            for digit_str in rev_digit_strs:
                if str(line[i:]).startswith(digit_str):
                    second_digit = rev_digit_dict[digit_str]
                    break
            
            if second_digit != None:
                break
            
            if char.isdigit():
                second_digit = int(char)
                break
        res += int(str(first_digit) + str(second_digit))

    print(res)