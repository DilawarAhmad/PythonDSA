
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
        
    def print_list(self,head):
        curr = head
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        print(res)
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)
head.next.next.next.next = ListNode(10)
head.next.next.next.next.next = ListNode(11)
head.next.next.next.next.next.next = ListNode(12)

node = head.next   # the node with value 5
sol = Solution()
sol.print_list(head)
sol.deleteNode(node)
sol.print_list(head)
sol.deleteNode(node)
sol.print_list(head)