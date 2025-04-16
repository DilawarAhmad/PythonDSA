def group(s):
    dic = {}
    for word in s:
        item =tuple(sorted(word))
        if item not in dic:
            dic[item] = []
        dic[item].append(word)
    return list(dic.values())
print(group(s=["tea","eat","sat","tae"]))