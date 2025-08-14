class Solution:
    def  towerOfHanoi(self, n, fromm, to, aux):
        if n == 1:
            print(f"Move disk 1 from {fromm} to {to}")
            return 1
        moves1 = self.towerOfHanoi(n - 1, fromm, aux, to)
        print(f"Move disk {n} from {fromm} to {to}")
        moves2 = 1
        moves3 = self.towerOfHanoi(n - 1, aux, to, fromm) 
        return moves1 + moves2 + moves3
sol = Solution()
print(sol.towerOfHanoi(3, 'A', 'C', 'B'))