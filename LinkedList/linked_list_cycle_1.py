class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
