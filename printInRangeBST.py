class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def printNearNodes(self, root, low, high):
        result =[]
        self.rangePrint(root,low,high,result)
        return result
    def rangePrint(self,root,low,high,result):
        if root is None:
            return None
        if root.val < low:
            self.rangePrint(root.right,low,high,result)
        elif root.val > high:
            self.rangePrint(root.left,low,high,result)
        else:
            self.rangePrint(root.left,low,high,result)
            result.append(root.val)
            self.rangePrint(root.right,low,high,result)


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(10)

sol = Solution()
print(sol.printNearNodes(root, 4, 9))  # [4, 5, 8]
print(sol.printNearNodes(root, 2, 10))  # [2, 3, 4, 5, 8, 10]
print(sol.printNearNodes(root, 11, 15))  # []
root = Node(5)
print(sol.printNearNodes(root, 3, 6))  # [5]
