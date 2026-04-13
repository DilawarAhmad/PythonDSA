class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        set_vo = ("a","e","i","o","u")
        fixed = list(s[:k])
        count = 0
        
        for char in fixed:
            if char in set_vo:
                count+=1
        max_count = count 
        for char in s[k:]:
            fixed.append(char)
            if char in set_vo:
                count+=1
            removed = fixed.pop(0)
            if removed in set_vo:
                count-=1
            max_count = max(max_count , count)


        return max_count


