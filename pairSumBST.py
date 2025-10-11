
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


class Solution:
    def findTarget(self, root, target): 
        list1 = []
        sorted_list =self.inOrder(root,list1)
        return self.twoSum(sorted_list,target)


    def inOrder(self,root,list1):
        if root is None:
            return list1
        self.inOrder(root.left,list1)
        list1.append(root.data)
        self.inOrder(root.right,list1)
        return list1

    def twoSum(self,sorted_list,target):
        left = 0
        right = len(sorted_list)-1
        while left < right:
            curr_sum = sorted_list[left] + sorted_list[right]
            if curr_sum==target:
                return True
            elif curr_sum<target:
                left+=1
            else:
                right-=1
        return False
    

root = Node(5)
root.left = Node(3)
root.right = Node(6)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(7)

ob = Solution()
print(ob.findTarget(root, 9))  # True
print(ob.findTarget(root, 28))  # False
print(ob.findTarget(root, 11))  # True
root2 = Node(5)
print(ob.findTarget(root2, 10))  # False
root3 = Node(0)
root3.left = Node(-2)
root3.left.right = Node(-1)
root3.right = Node(3)
print(ob.findTarget(root3, 2))  # True
print(ob.findTarget(None, 5))  # False
