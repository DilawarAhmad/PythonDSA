class Solution:

	def findMaximum(self, arr):
		first = 0
		last = len(arr) -1
		result = 0
		while first < last:
			mid = (first + last) //2
			if arr[mid] > arr[mid -1]:
				result = max(result,arr[mid])
				first =mid + 1
			else:
				result =max(result, arr[mid - 1])
				last = mid -1
		return result
sol = Solution()
print(sol.findMaximum([1, 3, 8, 12, 4, 2])) 
print(sol.findMaximum( [1, 2, 4, 5, 7, 8, 3]))
print(sol.findMaximum( [120, 100, 80, 20, 0]))
print(sol.findMaximum([1,15 ,25 ,45, 42 ,21 ,17, 12, 11]))