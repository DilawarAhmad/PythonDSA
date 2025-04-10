def reverseWords( s: str) -> str:
    result =' '.join(s.split()[::-1])
    return result
print(reverseWords(s="  this is   my name  "))
