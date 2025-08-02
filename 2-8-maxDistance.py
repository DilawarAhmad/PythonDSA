class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        dic = {}
        for i,num in enumerate(arr):
            if num not  in dic:
                dic[num] = [i]
            else:
                dic[num].append(i)
        max_len = 0
        for value in dic.values():
            if len(value) >1:
                max_len = max(value[-1] - value[0],max_len)
        return max_len + 1
    
sol = Solution()
print(sol.maxDistance([1, 2, 3, 4, 5]))
print(sol.maxDistance([1, 2, 1, 2, 1]))
print(sol.maxDistance([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))