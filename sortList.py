
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        slow , fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        right = mid.next
        mid.next = None
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right)
        return self.merge(left_sorted,right_sorted)

    def merge(self,left,right):
        dummy = ListNode(0)
        tail = dummy
        while left!=None and right!=None:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return dummy.next


