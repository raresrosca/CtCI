from linked_list_guy import LinkedList

def is_palindrome(ll):
    """O(n^2)"""
    current = ll.head
    while current.next:
        runner = current
        while runner.next.next:
            runner = runner.next
        if current.value != runner.next.value:
            return False
        else:
            current = current.next
            runner.next = None
    return True

def is_palindrome_2(ll):
    """O(n)"""
    current = ll.head
    a = ""
    while current:
        a += str(current.value)
        current = current.next

    for i in range(len(a)):
        if(a[i] != a[-i-1]):
            return False
    return True




if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.add_multiple([1, 2, 3, 3, 2, 1])

    ll2 = LinkedList()
    ll2.add_multiple([1, 2, 3, 7, 3, 2, 1])

    ll3 = LinkedList()
    ll3.add_multiple([1, 2, 3, 5])

    print(is_palindrome(ll1))
    print(is_palindrome(ll2))
    print(is_palindrome(ll3))

    ll1 = LinkedList()
    ll1.add_multiple([1, 2, 3, 3, 2, 1])

    ll2 = LinkedList()
    ll2.add_multiple([1, 2, 3, 7, 3, 2, 1])

    ll3 = LinkedList()
    ll3.add_multiple([1, 2, 3, 5])

    print(is_palindrome_2(ll1))
    print(is_palindrome_2(ll2))
    print(is_palindrome_2(ll3))