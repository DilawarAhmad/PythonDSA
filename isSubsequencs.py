def isSub(s,t):
    i=0
    j=0
    while i <len(s) and j<len(t):
        if s[i]==t[j]:
            i = i+1
            j= j+1
        else:
            j= j+1
    return i==len(s)
print(isSub(s="abc",t="abcdef"))