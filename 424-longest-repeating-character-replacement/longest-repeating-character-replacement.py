class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        ans = 0
        dict1 = {}
        for right in range(len(s)):
            if s[right] in dict1:
                dict1[s[right]]+=1
            else:
                dict1[s[right]] =1
            max_count = max(max_count, dict1[s[right]])
            while (right-left+1) - max_count > k:
                dict1[s[left]]-=1
                left+=1
            ans = max(ans , right-left+1)
        return ans
