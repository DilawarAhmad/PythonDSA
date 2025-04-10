def minimumParentheses(pattern):
    openBrac = 0
    count = 0
    for char in pattern:
        if char=="(":
            openBrac+=1
        else:
            if openBrac>0:
                openBrac-=1
            else:
                count +=1
    count +=openBrac
    return count
print(minimumParentheses(pattern="(((()"))