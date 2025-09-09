
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head, x: int):
        bef_head = ListNode(0)
        aft_head = ListNode(0)
        before = bef_head
        after = aft_head
        curr = head
        while curr:
            nxt = curr.next
            curr.next = None
            if curr.val < x:
                before.next = curr
                before = before.next
            else:
                after.next = curr
                after = after.next
            curr = nxt
        before.next = aft_head.next
        return bef_head.next

sol = Solution()

# Test Case 1: [1,4,3,2,5,2], x = 3
head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(2)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(2)

# Call
print(sol.partition(head1, 3))


# Test Case 2: [1,2,2], x = 3
head2 = ListNode(1)
head2.next = ListNode(2)
head2.next.next = ListNode(2)

print(sol.partition(head2, 3))


# Test Case 3: [3,4,5], x = 3
head3 = ListNode(3)
head3.next = ListNode(4)
head3.next.next = ListNode(5)

print(sol.partition(head3, 3))


# Test Case 4: Empty list, [], x = 1
head4 = None

print(sol.partition(head4, 1))


# Test Case 5: [1], x = 2
head5 = ListNode(1)

print(sol.partition(head5, 2))


# Test Case 6: [2,1], x = 2
head6 = ListNode(2)
head6.next = ListNode(1)

print(sol.partition(head6, 2))
