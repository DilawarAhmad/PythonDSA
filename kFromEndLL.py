'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
class Solution:
    def getKthFromLast(self, head, k):
        length = 0
        current = head
        while current:
            length+=1
            current = current.next
        position = length - k
        start = 0
        if position<=0:
            return -1
        while current is not None and start+1!=position:
            start+=1
            current = current.next
        if current is None:
            return -1
        else:
            return current.next.data
                