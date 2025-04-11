def firstUniqChar( s: str) -> int:
    dic = {}
    for char in s:
        if char in dic:
            dic[char] += 1
        else:
            dic[char] = 1
    item = None
    for key, value in dic.items():
        if value==1:
            item = key
            break
    if item is None:
        return -1
    for i in range(len(s)):
        if s[i]==item:
            return i
    return -1
print(firstUniqChar(s="aabbloveleetcode"))