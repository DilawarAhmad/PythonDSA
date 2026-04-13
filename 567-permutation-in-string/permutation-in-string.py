class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter()
        k =len(s1)
        for i in range(len(s2)):
            s2_count[s2[i]] += 1
            if i >= k:
                if s2_count[s2[i-k]] == 1:
                    del s2_count[s2[i-k]]
                else:
                    s2_count[s2[i-k]]-=1
            if s1_count == s2_count:
                return True 
        return False