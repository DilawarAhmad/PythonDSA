from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic ={}
        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1
        new_list = [[] for _ in range(len(nums)+1)]
        for num,freq in dic.items():
            new_list[freq].append(num)
        result = []
        count = 0
        for group in new_list[::-1]:
            for num in group:
                result.append(num)
                count += 1
                if count == k:
                    return result

            
sol = Solution()
print(sol.topKFrequent(nums=[1,2],k=2))