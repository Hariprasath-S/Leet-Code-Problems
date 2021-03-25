class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        while p:
            if p.child is None:
                p = p.next
                continue
            temp = p.child
            while temp.next:
                temp = temp.next
            temp.next = p.next
            if p.next:
                p.next.prev = temp
            p.next = p.child
            p.child.prev = p
            p.child = None
        return head
