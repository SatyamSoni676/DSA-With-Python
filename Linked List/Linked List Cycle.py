#https://leetcode.com/problems/linked-list-cycle/

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow, fast = head, head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False 
            slow = slow.next
            fast = fast.next.next

        return True
