# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:    
        if head.next == None:
            return True
        if head.next.next == None:
            return True if head.val == head.next.val else False
        
        slow = head
        fast = head
        
        while(fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
        
        if fast.next:
            slow.next = ListNode(10, slow.next)
            slow = slow.next
            fast = fast.next
        
        prev_ = slow
        slow, prev_.next = slow.next, None
        
        while(slow):
            next_ = slow.next
            slow.next = prev_
            prev_ = slow
            slow = next_
        
        ptr_1, ptr_2 = head, fast
        while(ptr_1 and ptr_2 and ptr_1.val == ptr_2.val):
            ptr_1, ptr_2 = ptr_1.next, ptr_2.next
        
        check = ptr_1 if ptr_1 else ptr_2
        if check and check.val != 10:
            return False
        return True