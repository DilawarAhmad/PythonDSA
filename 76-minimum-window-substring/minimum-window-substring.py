class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        target = {}
        window = {}
        left = 0 
        for char in t:
            target[char] = target.get(char,0) +1
        required = len(target)
        formed = 0
        min_len = float('inf')
        min_str = ""
        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char,0)+1
            if char in target and target[char] == window[char]:
                formed +=1
            while formed == required:
                window_size =right - left +1
                if window_size <min_len:
                    min_len = window_size
                    min_str = s[left:right+1]
                left_char = s[left]
                window[left_char]-=1
                if left_char in target and window[left_char] < target[left_char]:
                    formed -=1
                left+=1
        return min_str
