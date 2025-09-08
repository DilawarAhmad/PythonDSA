
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    def getKthFromLast(self, head, k):
        length = 0
        dummy = Node(0)
        dummy.next = head
        current = dummy
        while current:
            length+=1
            current = current.next
        position = length - k
        start = 0
        curr = dummy
        while curr:
            start+=1
            if start==position and curr.next:
                curr.next = curr.next.next
                break
            else:
                curr = curr.next
        return dummy.next
    