#User function Template for python3

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def transformTree(self, root):
        result =[0]
        self.revInorder(root,result)
        return root
    def revInorder(self,root,result):
        if root is None:
            return
        self.revInorder(root.right,result)
        prev_data = root.data
        root.data = result[0]
        result[0]+=prev_data
        self.revInorder(root.left,result)
# Helper function to print inorder traversal
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.data] + inorder(root.right)

# Helper function to create a BST manually
def create_tree_1():
    # Tree:
    #        11
    #       /  \
    #      2    29
    #     / \   / \
    #    1  7  15  40
    #             \
    #             45
    root = Node(11)
    root.left = Node(2)
    root.right = Node(29)
    root.left.left = Node(1)
    root.left.right = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(40)
    root.right.right.right = Node(45)
    return root

def create_tree_2():
    # Tree:
    #     5
    #    / \
    #   3   7
    #  / \   \
    # 2  4    8
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(8)
    return root

def create_tree_3():
    # Single node
    root = Node(10)
    return root

def create_tree_4():
    # Right skewed tree
    # 1 -> 2 -> 3 -> 4
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(3)
    root.right.right.right = Node(4)
    return root

def create_tree_5():
    # Left skewed tree
    # 4 -> 3 -> 2 -> 1
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    return root


# ---- TEST CASES ----
if __name__ == "__main__":
    sol = Solution()

    trees = [
        ("Test 1: Mixed BST", create_tree_1()),
        ("Test 2: Balanced BST", create_tree_2()),
        ("Test 3: Single Node", create_tree_3()),
        ("Test 4: Right Skewed", create_tree_4()),
        ("Test 5: Left Skewed", create_tree_5()),
    ]

    for name, tree in trees:
        print(f"\n{name}")
        print("Inorder before:", inorder(tree))
        sol.transformTree(tree)
        print("Inorder after: ", inorder(tree))
