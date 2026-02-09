# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            elements = []
            for _ in range(len(queue)):
                element = queue.popleft()
                elements.append(element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            result.append(elements)
        return result