class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        slow = fast = head
        index = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            if slow == fast:
                start = head
                while start != slow:
                    slow = slow.next
                    start = start.next
                return start
        return None
