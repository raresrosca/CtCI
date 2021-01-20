class StackOfPlates:
    def __init__(self, capacity):
        self.stack_capacity = capacity
        self.set_of_stacks = []
        self.stack = []
    
    def add(self, value):
        if len(self.stack) == self.stack_capacity:
            self.set_of_stacks.append(self.stack)
            self.stack = []
            self.stack.append(value)
        else:
            self.stack.append(value)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        elif not self.stack and not self.set_of_stacks:
            return None
        elif not self.stack and self.set_of_stacks:
            return self.set_of_stacks[-1][-1]
    
    def pop(self):
        if self.stack:
            self.stack.pop()
        elif not self.stack and not self.set_of_stacks:
            return None
        elif not self.stack and self.set_of_stacks:
            self.set_of_stacks[-1].pop()  
    
    def test(self):
        return self.set_of_stacks, self.stack



if __name__ == "__main__":
    s = StackOfPlates(5)
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    print(s.pop())
    s.add(5)
    s.add(6)
    s.add(7)
    print(s.pop())
    s.add(8)
    s.add(9)
    s.add(10)
    s.add(11)
    s.add(12)
    print(s.peek())
    print(s.test())
