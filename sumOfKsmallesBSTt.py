
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

    def summ(self,root, k):
        count = [0]
        result = [0]
        self.inOrder(root,k,count,result)
        return result[0]
    def inOrder(self,root,k,count,result):
        if root is None or count[0]>=k:
            return
        self.inOrder(root.left,k,count,result)
        if count[0] < k:
            count[0]+=1
            result[0]+=root.key
        if count[0]==k:
            return
        self.inOrder(root.right,k,count,result)


root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right = Node(9)

obj = Node(0)
print(obj.summ(root, 1))  # 2
print(obj.summ(root, 2))  # 2+3=5
print(obj.summ(root, 3))  # 2+3+4=9
print(obj.summ(root, 4))  # 2+3+4+5=14
print(obj.summ(root, 5))  # 2+3+4+5+8=22
print(obj.summ(root, 6))  # 2+3+4+5+8+9=31
