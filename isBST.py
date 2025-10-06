
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        return self.helper(root, float("-inf"),float("inf"))
    def helper(self,root,low,high):
        if root is None:
            return True
        if not (low< root.data <high):
            return False
        return self.helper(root.left,low,root.data) and self.helper(root.right,root.data,high)

    
root1 = Node(10)
root1.left = Node(5)
root1.right = Node(15)
print(Solution().isBST(root1))  # Expected: True

# Test Case 2: Invalid BST (left > root)
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
print(Solution().isBST(root2))  # Expected: False

# Test Case 3: Invalid BST (right < root)
root3 = Node(10)
root3.left = Node(5)
root3.right = Node(8)
print(Solution().isBST(root3))  # Expected: False

# Test Case 4: Single node
root4 = Node(10)
print(Solution().isBST(root4))  # Expected: True

# Test Case 5: Larger valid BST
root5 = Node(8)
root5.left = Node(3)
root5.right = Node(10)
root5.left.left = Node(1)
root5.left.right = Node(6)
root5.left.right.left = Node(4)
root5.left.right.right = Node(7)
root5.right.right = Node(14)
root5.right.right.left = Node(13)
print(Solution().isBST(root5))  # Expected: True