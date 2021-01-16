#Solved on leetcode

def detectCycle(self, head: ListNode) -> ListNode:
    """Using Dictionary"""
    a = {}
    while head:
        if head in a:
            return head
        else:
            a[head] = 1
        head = head.next

def detectCycle(self, head: ListNode) -> ListNode:
    """Tortoise and hare"""
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = head.next.next
    while slow!=fast:
        if fast is None or fast.next is None:
            return None
        slow = slow.next
        fast = fast.next.next
    slow = head  # This is the important bit. Once they intersect, set slow back to head and move them one at a time.
    while slow!=fast:
        slow = slow.next
        fast = fast.next
    return slow