class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n!=m:
            return False
        dict1 = {}
        for ch in s:
            if ch in dict1:
                dict1[ch]+=1
            else:
                dict1[ch] = 1
        for ch in t:
            if ch in dict1:
                dict1[ch]-=1
                if dict1[ch]==0:
                    del dict1[ch]
            else:
                return False
        return len(dict1)==0
