from linked_list_guy import LinkedList

def ll_sum_followup(ll1, ll2):
    c1 = ll1.head
    c2 = ll2.head
    a = b = 0
    while c1:
        a = a*10 + c1.value
        c1 = c1.next
    while c2:
        b = b*10 + c2.value
        c2 = c2.next
    
    p = a+b
    print("Follow-up values: ", a, b, p)
    new_ll = LinkedList()
    while p>=1:
        new_ll.add_to_beginning(p%10)
        p = int(p/10)
    return new_ll

def ll_sum(ll1, ll2):
    c1 = ll1.head
    c2 = ll2.head
    a = b = ""
    while c1:
        a += str(c1.value)
        c1 = c1.next
    while c2:
        b += str(c2.value)
        c2 = c2.next
    a = int(a[::-1])
    b = int(b[::-1])
    p = a + b
    print("Normal values: ", a, b, p)
    new_ll = LinkedList()
    while p>=1:
        new_ll.add(p%10)
        p = int(p/10)
    return new_ll


if __name__ == "__main__":
    ll_1 = LinkedList()
    ll_2 = LinkedList()
    ll_1.generate(3, 1, 9)
    ll_2.generate(3, 1, 9)
    new_ll1 = ll_sum(ll_1, ll_2)
    new_ll2 = ll_sum_followup(ll_1, ll_2)
    print(ll_1)
    print(ll_2)
    print("Normal: ", new_ll1)
    print("Follow-up: ", new_ll2)