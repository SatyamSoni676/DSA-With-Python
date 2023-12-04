#https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = head
        while curr is not None:
            next_node = curr.next
            curr.next = res
            res = curr
            curr = next_node
        return res