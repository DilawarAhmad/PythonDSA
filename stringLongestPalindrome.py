def longestPalindrome( s: str) -> int:
    dic = {}
    length =0
    odd_found = False
    for char in s:
        if char in dic:
            dic[char]+=1
        else:
            dic[char]= 1
    for key , value in dic.items():
        if value%2==0:
            length+=value
        if value%2!=0:
            length += value-1
            odd_found = True
    if odd_found:
        length +=1
    return length
print(longestPalindrome(s="abccccccddd"))