class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = Counter(nums)
        result = []
        new_arr = [[] for _ in range(len(nums) +1)]
        for num, count in dic.items():
            new_arr[count].append(num)
        for i in range(len(new_arr)-1,0,-1):
            for num in new_arr[i]:
                result.append(num)
                if len(result)==k:
                    return result