class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        result = []
        for num in nums:
            if num>0:
                positives.append(num)
            else:
                negatives.append(num)
        for x, y in zip(positives,negatives):
            result.append(x)
            result.append(y)
        return result
        