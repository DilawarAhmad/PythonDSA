'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

class Solution:
    def getMiddle(self, head):
        if head is None:
            return -1
        length = 0
        current = head
        while current:
            length+=1
            current =current.next
        current = head
        start = 0
        position = length//2
        while current and start != position:
            start+=1
            current = current.next
        return current.data
                
                
        
