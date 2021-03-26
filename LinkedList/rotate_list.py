class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        
        k = k%length
        cur.next = head
        temp = head
        for _ in range(length-k-1):
            temp = temp.next
        head = temp.next
        temp.next = None
        return head
