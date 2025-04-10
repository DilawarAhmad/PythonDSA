def decodeString(s: str) -> str:
    nums = []
    strings = []
    curr_num = 0
    curr_str = ''
    for char in s:
        if char.isdigit():
            curr_num = curr_num *10 + int(char)
        elif char =='[':
            nums.append(curr_num)
            strings.append(curr_str)
            curr_str=''
            curr_num = 0
        elif char ==']':
            multiple = nums.pop()
            prev_str = strings.pop()
            curr_str = prev_str +curr_str * multiple
        else:
            curr_str += char
    return curr_str
print(decodeString(s="3abc[2[pq]]"))