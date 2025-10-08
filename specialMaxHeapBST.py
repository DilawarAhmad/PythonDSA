#Convert BST to Max Heap
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    def convertToMaxHeapUtil(self, root):
        InorderList = []
        i =[0]
        self.Inorder(root, InorderList)
        self.createHeap(root, InorderList, i )


    def Inorder(self,root, InorderList):
        if root is None:
            return
        self.Inorder(root.left,InorderList)
        InorderList.append(root.data)
        self.Inorder(root.right, InorderList)

    def createHeap(self,root, revInorderList, i):
        if root is None:
            return i[0]
        
        self.createHeap(root.left, revInorderList, i)
        self.createHeap(root.right, revInorderList, i)
        root.data = revInorderList[i[0]]
        i[0] +=1
        return root


# Test Cases for Convert BST to Max Heap

# Helper function to print preorder traversal (for verification)
def postorder(root):
    return [] if root is None else postorder(root.left) + postorder(root.right)+[root.data] 

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
print("Test 1 (Balanced BST):", postorder(root1))  # Expected postorder of Max Heap

# Test Case 2: Left Skewed BST
root2 = Node(5)
root2.left = Node(4)
root2.left.left = Node(3)
root2.left.left.left = Node(2)
root2.left.left.left.left = Node(1)

sol = Solution()
sol.convertToMaxHeapUtil(root2)
print("Test 2 (Left Skewed BST):", postorder(root2))

# Test Case 3: Right Skewed BST
root3 = Node(1)
root3.right = Node(2)
root3.right.right = Node(3)
root3.right.right.right = Node(4)
root3.right.right.right.right = Node(5)

sol = Solution()
sol.convertToMaxHeapUtil(root3)
print("Test 3 (Right Skewed BST):", postorder(root3))

# Test Case 4: Single Node
root4 = Node(10)

sol = Solution()
sol.convertToMaxHeapUtil(root4)
print("Test 4 (Single Node):", postorder(root4))

# Test Case 5: Empty Tree
root5 = None

sol = Solution()
sol.convertToMaxHeapUtil(root5)
print("Test 5 (Empty Tree):", postorder(root5))
