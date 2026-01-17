class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for num,count in freq.items():
            heapq.heappush(heap,(count,-num))
        result = []
        while heap:
            count,neg_num = heapq.heappop(heap)
            result.extend([-neg_num]*count)
        return result
