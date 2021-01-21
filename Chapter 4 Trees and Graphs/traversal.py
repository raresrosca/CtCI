# Implement a binary search tree with insert and print methods.
# Implement in-order, pre-order and post-order traversal on the binary search tree.

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

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

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.data)
        if self.right:
            self.right.in_order_print()


    def pre_order_print(self):
        print(self.data)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()

    def post_order_print(self):
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.data)
        
if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(13)
    root.insert(15)
    root.insert(8)
    print("In order print: ")
    root.in_order_print()
    print("Pre-order print: ")
    root.pre_order_print()
    print("Post-order print: ")
    root.post_order_print()

    