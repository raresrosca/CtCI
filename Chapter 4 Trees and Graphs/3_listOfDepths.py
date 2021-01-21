from traversal import Node

class LinkedListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def add(self, value):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        values = [str(x) for x in self]
        return "->".join(values)
    

def minimal_tree(arr, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    n = Node(arr[mid])
    n.left = minimal_tree(arr, start, mid-1)
    n.right = minimal_tree(arr, mid+1, end)
    return n

def bfs(root):
    q = [root]
    list_of_llists = []
    while q:
        llist = LinkedList()
        llist.head = LinkedListNode(q.pop(0))
        length = len(q)
        for i in range(length):
            llist.add(q.pop(0))
        
        list_of_llists.append(llist)
        current = llist.head
        while current:
            if current.val.left is not None:
                q.append(current.val.left)
            if current.val.right is not None:
                q.append(current.val.right)
            current = current.next
    return list_of_llists


if __name__ == "__main__":
    n = 100
    arr = [i for i in range(n)]
    start = 0
    end = len(arr)-1
    min_tree = minimal_tree(arr, start, end)
    lists = bfs(min_tree)
    current = lists[3].head
    while current:
        print(current.val.data)
        current = current.next