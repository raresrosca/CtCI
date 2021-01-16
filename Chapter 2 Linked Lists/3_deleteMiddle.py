from linked_list_guy import LinkedList

def remove_middle(ll, keyword):
    if ll.head is None:
        return None

    current = ll.head
    
    while current.next.next:
        runner = current.next
        if runner.value == keyword:
            current.next = current.next.next
        else:
            current = current.next
    return ll



if __name__ == "__main__":
    ll = LinkedList()
    ll.generate(4, 0, 3)
    print(ll, "\n")
    keyword = 0
    new_ll = remove_middle(ll, keyword)
    print(new_ll)
    