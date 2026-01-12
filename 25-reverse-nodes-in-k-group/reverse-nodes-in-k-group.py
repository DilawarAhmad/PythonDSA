# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next =head
        prev = dummy
        while True:
            kth = prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            start = prev.next
            next_block = kth.next
            curr = start
            prev_node = next_block
            while curr!= next_block:
                temp = curr.next
                curr.next = prev_node
                prev_node = curr
                curr = temp
            prev.next = kth
            prev = start
