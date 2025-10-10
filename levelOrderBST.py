#Function to construct the BST from its given level order traversal.

class Node:
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None
def insertBST(root,val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insertBST(root.left,val)
    if val > root.val:
        root.right = insertBST(root.right,val)
    return root
def constructBst(arr,n):
    root = None
    for val in arr:
        root = insertBST(root,val)
    return root 


# Helper function for preorder traversal
def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)


# ---- Test Case 1 ----
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
n1 = len(arr1)
root1 = constructBst(arr1, n1)
print("Test 1 Preorder:", preorder(root1))
# Expected: [7, 4, 3, 1, 6, 5, 12, 8, 10]

# ---- Test Case 2 ----
arr2 = [1, 3, 4, 6, 7, 8]
n2 = len(arr2)
root2 = constructBst(arr2, n2)
print("Test 2 Preorder:", preorder(root2))
# Expected: [1, 3, 4, 6, 7, 8]

# ---- Test Case 3 ----
arr3 = [10, 5, 15, 2, 7, 12, 20]
n3 = len(arr3)
root3 = constructBst(arr3, n3)
print("Test 3 Preorder:", preorder(root3))
# Expected: [10, 5, 2, 7, 15, 12, 20]

# ---- Test Case 4 ----
arr4 = [5, 3, 8, 2, 4, 6, 9]
n4 = len(arr4)
root4 = constructBst(arr4, n4)
print("Test 4 Preorder:", preorder(root4))
# Expected: [5, 3, 2, 4, 8, 6, 9]

# ---- Test Case 5: Single element ----
arr5 = [42]
n5 = len(arr5)
root5 = constructBst(arr5, n5)
print("Test 5 Preorder:", preorder(root5))
# Expected: [42]

# ---- Test Case 6: Empty array ----
arr6 = []
n6 = len(arr6)
root6 = constructBst(arr6, n6)
print("Test 6 Preorder:", preorder(root6))
# Expected: []
