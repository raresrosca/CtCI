class Stack:
    def __init__(self):
        self.stack = []

    def __iter__(self):
        for i in self.stack:
            yield i

    def __str__(self):
        values = [str(i) for i in self.stack]
        return " ".join(values)

    def push(self, value):
        self.stack.append(value)

    def push_multiple(self, values):
        for i in values:
            self.stack.append(i)

    def pop(self):
        self.stack.pop()

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

def sort_stack(s):
    pass

if __name__ == "__main__":
    s = Stack()
    s.push_multiple([1, 4, 6, 2, 3, 9, 5, 7, 8, 0])
    print(s)
