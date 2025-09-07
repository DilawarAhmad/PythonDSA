
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            new =current.next
            current.next =prev
            prev = current
            current = new
        return prev