# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node, part = head, None
        while(node and node.val < x):
            part = node
            node = node.next
        
        while(node and node.next):
            nextNode = node.next.next
            if node.next.val < x:
                if part:
                    node.next.next = part.next
                    part.next = node.next
                else:   
                    node.next.next = head
                    head = node.next
                part = node.next
                node.next = nextNode
            else:   node = node.next
        
        return head