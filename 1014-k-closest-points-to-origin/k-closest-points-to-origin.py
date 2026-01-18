class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for num in points:
            x1 = num[0]
            y1 = num[1]
            distance = sqrt(x1**2 + y1**2)
            heapq.heappush(max_heap,(-distance,num))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        return [num for _ ,num in max_heap]