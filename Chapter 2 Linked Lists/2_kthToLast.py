from linked_list_guy import LinkedList

def kth_to_last(ll, k):
    if ll.head is None:
        return
    
    current = ll.head
    
    while current.next:
        runner = current
        distance = k
        while distance:
            runner = runner.next
            distance -= 1
            if runner.next == None:
                return current
        current = current.next
    
    return current


if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(30, 0, 9)
    k = 2
    kth = kth_to_last(ll, k)
    print(ll, '\n')
    print(kth.value)