def reverseStr(s, k):
    result = []
    for i in range(0,len(s),2*k):
        first = s[i:i+k][::-1]
        second = s[i+k:i+2*k]
        result.append(first+second)
    return ''.join(result)
print(reverseStr(s='abcd',k=2))
print(reverseStr(s='abcdef',k=2))
print(reverseStr(s='abcde',k=6))