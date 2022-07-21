# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        node, leftPrevNode = head, None
        
        if left == right:
            return head
        
        while(count < left):
            leftPrevNode = node
            node = node.next
            count += 1
        leftNode = node
        prevNode = node
        node = node.next
        count += 1
        
        nextNode = None
        while(count <= right):
            nextNode = node.next
            node.next = prevNode    
            prevNode = node
            node = nextNode
            count += 1
            
        leftNode.next = nextNode
        if leftPrevNode:
            leftPrevNode.next = prevNode
        else:   head = prevNode
        
        return head