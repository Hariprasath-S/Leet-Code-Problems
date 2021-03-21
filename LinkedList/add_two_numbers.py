class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = l1
        q = l2
        cur = dummy
        carry = 0
        while p or q or carry:            
            x = p.val if p else 0
            y = q.val if q else 0
            carry, out = divmod(x + y + carry,10)
            cur.next = ListNode(out);
            cur = cur.next
            p = p.next if p else None
            q = q.next if q else None
            
        return dummy.next
