class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children

    def __repr__(self):
        return self.data

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes

    def __iter__(self):
        for i in self.nodes:
            yield i.data

    def __repr__(self):
        values = [node.data for node in self]
        return values

if __name__ == "__main__":
    a = Node('a', [b, c])
    b = Node('b', [c])
    c = Node('c', [d])
    d = Node('d', [])
    g = Graph([a, b, c, d])
    print(g)
