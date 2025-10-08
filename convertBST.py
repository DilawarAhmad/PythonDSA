
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root):
        result =[0]
        self.revInorder(root,result)
        return root
    def revInorder(self,root,result):
        if root is None:
            return
        self.revInorder(root.right,result)
        result[0]+=root.val
        root.val = result[0]
        self.revInorder(root.left,result)
        
        
    
def inorderTraversal(root):
    if root is None:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

root1 = TreeNode(4)
root1.left = TreeNode(1)
root1.right = TreeNode(6, TreeNode(5), TreeNode(7))

sol = Solution()
new_root1 = sol.convertBST(root1)
print("Test 1:", inorderTraversal(new_root1))

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1))))
sol = Solution()
new_root2 = sol.convertBST(root2)
print("Test 2:", inorderTraversal(new_root2))

root3 = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
sol = Solution()
new_root3 = sol.convertBST(root3)
print("Test 3:", inorderTraversal(new_root3))

root4 = TreeNode(10)
sol = Solution()
new_root4 = sol.convertBST(root4)
print("Test 4:", inorderTraversal(new_root4))

root5 = None
sol = Solution()
new_root5 = sol.convertBST(root5)
print("Test 5:", inorderTraversal(new_root5))
