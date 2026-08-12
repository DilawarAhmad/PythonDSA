# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head2 = list2
        while head2.next:
            head2 = head2.next
        fast = list1
        for i in range(a-1):
            fast = fast.next
        slow = fast
        len3 = b-a+1
        for i in range(len3):
            fast = fast.next
        slow.next = list2
        head2.next = fast.next
        fast.next = None
        return list1