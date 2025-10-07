
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root):
        self.first = None
        self.second = None
        self.prev = TreeNode(float("-inf"))
        self.checkBST(root)
        if self.first and self.second:
            self.first.val , self.second.val = self.second.val , self.first.val

    def checkBST(self,root):
        if root is None:
            return
        self.checkBST(root.left)
        if (root.val < self.prev.val):
            if not self.first:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.checkBST(root.right)

# Helper function to do inorder traversal (to check result)
def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

# Helper functions to build test trees
def buildTree1():
    # Tree: 3,1,4,2 (swapped 2 and 3)
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(2)
    return root

def buildTree2():
    # Tree: 1,null,3,2 (swapped 1 and 3)
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    return root

def buildTree3():
    # Tree: 4,1,3,null,null,2 (swapped 2 and 4)
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(2)
    return root

def buildTree4():
    # Tree: 1,3,8,6,4 (swapped 6 and 1)
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(4)
    return root

def buildTree5():
    # Tree: 10,15,5,2,8,null,20 (swapped 5 and 15)
    root = TreeNode(10)
    root.left = TreeNode(15)
    root.right = TreeNode(5)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(8)
    root.right.right = TreeNode(20)
    return root

# Test harness
sol = Solution()

# Test 1
root1 = buildTree1()
sol.recoverTree(root1)
print("Test 1 Inorder:", inorderTraversal(root1))

# Test 2
root2 = buildTree2()
sol.recoverTree(root2)
print("Test 2 Inorder:", inorderTraversal(root2))

# Test 3
root3 = buildTree3()
sol.recoverTree(root3)
print("Test 3 Inorder:", inorderTraversal(root3))

# Test 4
root4 = buildTree4()
sol.recoverTree(root4)
print("Test 4 Inorder:", inorderTraversal(root4))

# Test 5
root5 = buildTree5()
sol.recoverTree(root5)
print("Test 5 Inorder:", inorderTraversal(root5))

        