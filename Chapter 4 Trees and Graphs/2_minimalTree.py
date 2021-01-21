
class Node:
    def __init__(self, value = None):
        self.data = value
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            self.data = value
    
    def in_order_print(self, ):
        if self.left:
            self.left.in_order_print()
        print(self.data)
        if self.right:
            self.right.in_order_print()

def minimal_tree(arr, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    n = Node(arr[mid])
    n.left = minimal_tree(arr, start, mid-1)
    n.right = minimal_tree(arr, mid+1, end)
    return n
    

if __name__ == "__main__":
    n = 100
    arr = [i for i in range(n)]
    start = 0
    end = len(arr)-1
    min_tree = minimal_tree(arr, start, end)
    print(min_tree.data)
    print(min_tree.left.data)
    print(min_tree.left.left.data)
    print(min_tree.left.left.left.data)
    print(min_tree.left.left.left.left.data)
    print(min_tree.left.left.left.left.left.right.data)
    print(min_tree.left.left.left.left.right.data)
