# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        k %=n
        if k==0:
            return head
        slow = head
        fast = head
        total_l = n-k
        for i in range(total_l-1):
            slow = slow.next
        fast = slow.next
        new_head = fast
        slow.next = None
        while fast.next:
            fast = fast.next
        fast.next = head
        head = new_head
        return head
