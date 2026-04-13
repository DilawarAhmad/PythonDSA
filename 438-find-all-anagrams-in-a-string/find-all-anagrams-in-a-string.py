class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        w_count = Counter()
        leng = len(p)
        result = []
        for i in range(len(s)):
            w_count[s[i]] +=1
            if i >= leng:
                if w_count[s[i-leng]] == 1:
                    del w_count[s[i-leng]]
                else:
                    w_count[s[i-leng]] -= 1
            if w_count == p_count:
                result.append(i-leng+1)
        return result
            