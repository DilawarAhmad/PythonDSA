#User function Template for python3

#LinkedList Node
class LNode:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        
      
class TNode:
    def __init__(self, data):
        self.data=data
        self.left = self.right = None

class Solution:
    def sortedListToBST(self, head):
        result = []
        preorder = []
        while head is not None:
            result.append(head.data)
            head = head.next
        low = 0
        high = len(result)-1
        root = self.createBST(result,low,high)
        self.preOrder(root,preorder)
        return preorder
    
    def createBST(self,result,low,high):
        if low>high:
            return None
        mid = (low+high+1)//2
        node = TNode(result[mid])
        node.left = self.createBST(result,low,mid-1)
        node.right = self.createBST(result,mid+1,high)
        return node
    
    def preOrder(self,root,preorder):
        if root is None:
            return
        preorder.append(root.data)
        self.preOrder(root.left,preorder)
        self.preOrder(root.right,preorder)


# Assuming the provided code is already defined above this (LNode, TNode, Solution)

def create_linked_list(arr):
    """Helper function to create a linked list from a list."""
    if not arr:
        return None
    head = LNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = LNode(val)
        current = current.next
    return head

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: Odd number of nodes
    head1 = create_linked_list([-10, -3, 0, 5, 9])
    print("Test 1 (Odd length):", sol.sortedListToBST(head1))
    # Expected Preorder (may vary slightly due to structure): [0, -10, -3, 5, 9]

    # Test Case 2: Even number of nodes
    head2 = create_linked_list([1, 2, 3, 4])
    print("Test 2 (Even length):", sol.sortedListToBST(head2))
    # Expected Preorder: [2, 1, 3, 4] or [3, 2, 1, 4] depending on mid calculation

    # Test Case 3: Single node
    head3 = create_linked_list([5])
    print("Test 3 (Single node):", sol.sortedListToBST(head3))
    # Expected Preorder: [5]

    # Test Case 4: Two nodes
    head4 = create_linked_list([1, 2])
    print("Test 4 (Two nodes):", sol.sortedListToBST(head4))
    # Expected Preorder: [1, 2] or [2, 1]

    # Test Case 5: Negative and positive numbers
    head5 = create_linked_list([-5, -2, 0, 3, 8])
    print("Test 5 (Mixed values):", sol.sortedListToBST(head5))
    # Expected Preorder: [0, -5, -2, 3, 8]

    # Test Case 6: Empty linked list
    head6 = create_linked_list([])
    print("Test 6 (Empty list):", sol.sortedListToBST(head6))
    # Expected Preorder: []
