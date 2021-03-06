class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow = head
        fast = head

        for i in range(n):
            fast = fast.next
        
        if fast is None:
            return head.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head
