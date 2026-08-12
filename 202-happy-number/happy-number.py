class Solution:
    def isHappy(self, n: int) -> bool:
        slow = self.square(n)
        fast = self.square(self.square(n))
        while slow != fast:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
        return slow == 1
    def square(self,n):
        ans = 0
        while n>0:
            x = n%10
            ans += x**2
            n = n//10
        return ans
            