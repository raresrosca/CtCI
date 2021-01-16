from linked_list_guy import LinkedList

def getIntersectionNode(ll1, ll2):
    """Using a dictionary"""
    headA = ll1.head
    headB = ll2.head
    a = {}
    while headA:
        a[headA] = 1
        headA = headA.next
    while headB:
        if headB in a:
            return headB
        headB = headB.next
    return None

def intersection(list1, list2):
    """Difference in length, constant memory """

    if list1.tail != list2.tail:
        return False
    
    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for i in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


