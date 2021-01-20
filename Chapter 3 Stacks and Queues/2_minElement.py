class Stack:
    def __init__(self):
        self.stack = []
        self.mins_array = []
    
    def add(self, value):
        if self.stack:
            self.stack.append(value)
            if self.stack[self.mins_array[-1]] > value:
                self.mins_array.append(len(self.stack)-1)
        else:
            self.stack.append(value)
            self.mins_array.append(1)

    def pop(self):
        if self.mins_array[-1] == len(self.stack) - 1:
            self.stack.pop()
            self.mins_array.pop()
        else:
            self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.stack[self.mins_array[-1]]

if __name__ == "__main__":
    s = Stack()
    s.add(7)
    s.add(5)
    print(s.min()) #5
    s.add(8)
    s.add(3)
    print(s.min()) #3
    s.add(2)
    print(s.min()) #2
    s.pop()
    print(s.min()) #3
    s.pop()
    print(s.min()) #5

