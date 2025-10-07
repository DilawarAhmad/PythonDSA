
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Solution:
    # The given root is the root of the Binary Tree
    # Return the root of the generated BST
    def binaryTreeToBST(self, root):
        sorted = []
        sortedList = self.inOrder(root, sorted)
        sortedList.sort()
        i = [0]
        self.createBST(root,sortedList,i)

    def inOrder(self,root,sorted):
        if root is None:
            return
        self.inOrder(root.left,sorted)
        sorted.append(root.data)
        self.inOrder(root.right,sorted)
        return sorted
    def createBST(self,root,sortedList,i):
        if root is None:
            return
        
        self.createBST(root.left,sortedList,i)
        root.data = sortedList[i[0]]
        i[0]+=1
        self.createBST(root.right,sortedList,i)
            
        return root


def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.data] + inorderTraversal(root.right)

def buildTree1():
    # Tree:
    #     10
    #    /  \
    #   2    7
    #  / \
    # 8   4
    root = Node(10)
    root.left = Node(2)
    root.right = Node(7)
    root.left.left = Node(8)
    root.left.right = Node(4)
    return root
def buildTree2():
    # Tree:
    #     3
    #    / \
    #   1   2
    root = Node(3)
    root.left = Node(1)
    root.right = Node(2)
    return root

def buildTree3():
    # Tree:
    #      5
    #     / \
    #    3   6
    #   / \
    #  2   4
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    return root

def buildTree4():
    # Tree:
    # 1 -> 2 -> 3 -> 4 (right skewed)
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    return root

def buildTree5():
    # Tree:
    #       10
    #      /  \
    #     30   15
    #    /      \
    #   20       5
    root = Node(10)
    root.left = Node(30)
    root.right = Node(15)
    root.left.left = Node(20)
    root.right.right = Node(5)
    return root

sol = Solution()

# Test 1
root1 = buildTree1()
sol.binaryTreeToBST(root1)
print("Test 1 Inorder:", inorderTraversal(root1))

# Test 2
root2 = buildTree2()
sol.binaryTreeToBST(root2)
print("Test 2 Inorder:", inorderTraversal(root2))

# Test 3
root3 = buildTree3()
sol.binaryTreeToBST(root3)
print("Test 3 Inorder:", inorderTraversal(root3))

# Test 4
root4 = buildTree4()
sol.binaryTreeToBST(root4)
print("Test 4 Inorder:", inorderTraversal(root4))

# Test 5
root5 = buildTree5()
sol.binaryTreeToBST(root5)
print("Test 5 Inorder:", inorderTraversal(root5))
