# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        result = []
        l_r = True
        while queue:
            level = []
            for _ in range(len(queue)):
                element = queue.popleft()
                if l_r:
                    level.append(element.val)
                else:
                    level.insert(0,element.val)
                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
            l_r = not l_r
            result.append(level)
        return result
