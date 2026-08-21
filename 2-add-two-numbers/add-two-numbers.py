# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        head1 = l1
        head2 = l2
        while head1:
            num1.append(head1.val)
            head1 = head1.next
        while head2:
            num2.append(head2.val)
            head2 = head2.next
        num1 = num1[::-1]
        num2 = num2[::-1]
        num3= "".join(map(str,num1))
        num4 = "".join(map(str,num2))
        sum_ = list(str(int(num3)+int(num4)))
        sum_ = sum_[::-1]
        dummy = ListNode(-1)
        head = dummy
        for i in range(len(sum_)):
            element = ListNode(int(sum_[i]))
            head.next = element
            head = head.next
        return dummy.next
