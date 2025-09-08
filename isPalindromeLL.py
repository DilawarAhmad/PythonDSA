from collections import deque
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head) -> bool:
        queue = deque()
        curr = head
        while curr:
            queue.append(curr.val)
            curr = curr.next
        for i in range(len(queue)//2):
            if queue.popleft() != queue.pop():
                return False
        return True
def print_list(head):
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    print(res)
sol = Solution()
# Test Case 1: Palindrome list [1, 2, 2, 1]
head1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)
head1.next = node2
node2.next = node3
node3.next = node4
print("List 1:", end=" "); print_list(head1)
print(sol.isPalindrome(head1))

# Test Case 2: Palindrome list [1, 2, 3, 2, 1]
head2 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)
head2.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
print("List 2:", end=" "); print_list(head2)
print(sol.isPalindrome(head2))

# Test Case 3: Non-palindrome list [1, 2]
head3 = ListNode(1)
node2 = ListNode(2)
head3.next = node2
print("List 3:", end=" "); print_list(head3)
print(sol.isPalindrome(head3))

# Test Case 4: Single element [1] (always palindrome)
head4 = ListNode(1)
print("List 4:", end=" "); print_list(head4)
print(sol.isPalindrome(head4))

# Test Case 5: Empty list [] (considered palindrome)
head5 = None
print("List 5:", head5)  # None
print(sol.isPalindrome(head5))
