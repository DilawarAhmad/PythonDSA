class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap = []
        for i in range(len(score)):
            heapq.heappush(heap,(-score[i],i))
        result = [""]*len(score)
        for i in range(len(score)):
            element , index = heapq.heappop(heap)
            if -element in score and i==0:
                result[index] = "Gold Medal"
            elif -element in score and i==1:
                result[index] = "Silver Medal"
            elif -element in score and i==2:
                result[index] = "Bronze Medal"
            else:
                element = i+1
                result[index] = str(element)
        return result
            
