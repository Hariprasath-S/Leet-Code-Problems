class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        node = None
        while slow:
            next = slow.next
            slow.next = node
            node = slow
            slow = next
        while node:
            if head.val!=node.val:
                return False
            node = node.next
            head = head.next
        return True
