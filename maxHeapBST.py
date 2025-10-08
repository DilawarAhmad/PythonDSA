#Convert BST to Max Heap
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def convertToMaxHeapUtil(self, root):
        revInorderList = []
        i =[0]
        self.revInorder(root, revInorderList)
        self.createHeap(root, revInorderList, i )


    def revInorder(self,root, revInorderList):
        if root is None:
            return
        self.revInorder(root.right,revInorderList)
        revInorderList.append(root.data)
        self.revInorder(root.left, revInorderList)

    def createHeap(self,root, revInorderList, i):
        if root is None:
            return i[0]
        root.data = revInorderList[i[0]]
        i[0] +=1
        self.createHeap(root.right, revInorderList, i)
        self.createHeap(root.left, revInorderList, i)
        return root


# Test Cases for Convert BST to Max Heap

# Helper function to print preorder traversal (for verification)
def preorder(root):
    return [] if root is None else [root.data] + preorder(root.right) + preorder(root.left)

# Test Case 1: Simple BST
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(6)
root1.left.left = Node(1)
root1.left.right = Node(3)
root1.right.left = Node(5)
root1.right.right = Node(7)

sol = Solution()
sol.convertToMaxHeapUtil(root1)
print("Test 1 (Balanced BST):", preorder(root1))  # Expected preorder of Max Heap

# Test Case 2: Left Skewed BST
root2 = Node(5)
root2.left = Node(4)
root2.left.left = Node(3)
root2.left.left.left = Node(2)
root2.left.left.left.left = Node(1)

sol = Solution()
sol.convertToMaxHeapUtil(root2)
print("Test 2 (Left Skewed BST):", preorder(root2))

# Test Case 3: Right Skewed BST
root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
root3.right.right.right = Node(4)
root3.right.right.right.right = Node(5)

sol = Solution()
sol.convertToMaxHeapUtil(root3)
print("Test 3 (Right Skewed BST):", preorder(root3))

# Test Case 4: Single Node
root4 = Node(10)

sol = Solution()
sol.convertToMaxHeapUtil(root4)
print("Test 4 (Single Node):", preorder(root4))

# Test Case 5: Empty Tree
root5 = None

sol = Solution()
sol.convertToMaxHeapUtil(root5)
print("Test 5 (Empty Tree):", preorder(root5))
