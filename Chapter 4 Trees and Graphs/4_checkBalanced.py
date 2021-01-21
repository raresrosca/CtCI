import math 

class Node:
    def __init__(self, value):
        self.data = value
        self.right = None
        self.left = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

def height(node):
    if node is None:
        return -1
    
    h1 = height(node.left)
    if h1 == -math.inf:
        return -math.inf

    h2 = height(node.right)
    if h2 == -math.inf:
        return -math.inf

    if abs(h1-h2) > 1:
        return -math.inf
    else:
        return max(height(node.left), height(node.right)) + 1




if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    g = Node('g')
    h = Node('h')
    i = Node('i')
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    d.left = f
    c.left = g
    c.right = h
    g.left = i
    print(height(a))

