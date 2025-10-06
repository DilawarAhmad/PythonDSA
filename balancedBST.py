
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def balanceBST(self,root):
        result = []
        self.inOrder(root,result)
        balanced = self.balance(result,0,len(result)-1)
        return self.calculate(balanced)
    def inOrder(self,root,result):
        if root is None:
            return
        self.inOrder(root.left,result)
        result.append(root.data)
        self.inOrder(root.right,result)
    def balance(self,result,start,end):
        if start>end:
            return None
        mid = (start+end)//2
        node = Node(result[mid])
        node.left = self.balance(result,start,mid-1)
        node.right = self.balance(result, mid+1, end)
        return node
    def calculate(self,node):
        if node is None:
            return 0 
        return 1+ max(self.calculate(node.left), self.calculate(node.right))


# ------------------ TEST CASES ------------------
solution = Solution()

# Test Case 1: Basic BST
root1 = Node(2)
root1.left = Node(1)
root1.right = Node(3)
print("Height of balanced BST (Test 1):", solution.balanceBST(root1))

# Test Case 2: Right-skewed BST
root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)
root2.right.right.right = Node(4)
print("Height of balanced BST (Test 2):", solution.balanceBST(root2))

# Test Case 3: Left-skewed BST
root3 = Node(4)
root3.left = Node(3)
root3.left.left = Node(2)
root3.left.left.left = Node(1)
print("Height of balanced BST (Test 3):", solution.balanceBST(root3))

# Test Case 4: Random BST
root4 = Node(5)
root4.left = Node(3)
root4.right = Node(8)
root4.left.left = Node(2)
root4.left.right = Node(4)
root4.right.right = Node(9)
print("Height of balanced BST (Test 4):", solution.balanceBST(root4))

# Test Case 5: Single Node
root5 = Node(10)
print("Height of balanced BST (Test 5):", solution.balanceBST(root5))