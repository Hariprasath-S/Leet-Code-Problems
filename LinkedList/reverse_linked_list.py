class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr      
        return curr
