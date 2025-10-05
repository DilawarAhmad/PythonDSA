
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        count = [0]
        result = [-1]
        self.inOrder(root,k,count,result)
        return result[0]

    def inOrder(self,root,k,count,result):
        if root is None or count[0]>= k:
            return 
        self.inOrder(root.left,k,count,result)

        count[0] += 1
        if count[0] == k:
            result[0]  = root.val
            return
        
        self.inOrder(root.right,k,count,result)


def test():
    sol = Solution()
    
    # Test 1
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    print(sol.kthSmallest(root, 1))  # Expected 1
    
    # Test 2
    print(sol.kthSmallest(root, 3))  # Expected 3

    # Test 3
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(6)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(4)
    root2.left.left.left = TreeNode(1)
    print(sol.kthSmallest(root2, 2))  # Expected 2

    # Test 4
    root3 = TreeNode(8)
    root3.left = TreeNode(4)
    root3.right = TreeNode(10)
    root3.left.left = TreeNode(2)
    root3.left.right = TreeNode(6)
    print(sol.kthSmallest(root3, 5))  # Expected 10

    # Test 5
    print(sol.kthSmallest(None, 1))  # Expected -1

test()
