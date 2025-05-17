class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen_set = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in seen_set:
                seen_set.remove(s[left])
                left+=1
            seen_set.add(s[right])
            max_len = max(max_len,right-left+1)
        return max_len
    
sol = Solution()
print(sol.lengthOfLongestSubstring(s="abcabcbb"))
