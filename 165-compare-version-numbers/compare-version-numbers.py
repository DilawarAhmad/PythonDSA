class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        int1 = [int(x) for x in version1.split(".")]
        int2 = [int(x) for x in version2.split(".")]
        n = len(int1)
        m = len(int2)
        i = j = 0
        while i<n or j<m:
            if i<n and j<m and int1[i] > int2[j]:
                return 1
            elif i<n and j<m and int1[i] < int2[j]:
                return -1
            elif i<n and j>=m and int1[i] > 0:
                return 1
            elif i>=n and j<m and int2[j] > 0:
                return -1
            else:
                i+=1
                j+=1
                continue
        return 0
        
            