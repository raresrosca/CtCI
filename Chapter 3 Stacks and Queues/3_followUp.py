class StackOfPlates:
    def __init__(self, capacity):
        self.stack_capacity = capacity
        self.set_of_stacks = []
        self.stack = []
        self.len_set = 0
    
    def add(self, value):
        if len(self.stack) == self.stack_capacity:
            self.set_of_stacks.append(self.stack)
            self.stack = []
            self.stack.append(value)
            self.len_set += 1
        else:
            self.stack.append(value)

    def peek(self):
        if self.stack:
            return self.stack[-1]
        elif not self.stack and not self.set_of_stacks:
            return None
        elif not self.stack and self.set_of_stacks:
            return self.set_of_stacks[-1][-1]
    
    def pop(self, idx):
        if idx == 0:
            if self.set_of_stacks[0]:
                self.set_of_stacks[0].pop()
            elif not self.set_of_stacks[0] and self.stack:
                self.stack.pop()
        else:
            if idx < self.len_set:
                self.set_of_stacks[idx].pop()
            elif idx < self.len_set+1 and self.stack:
                self.stack.pop()

    
    def test(self):
        return self.set_of_stacks, self.stack



if __name__ == "__main__":
    s = StackOfPlates(4)
    s.add(1)
    s.add(2)
    s.add(3)
    s.add(4)
    s.add(5)
    s.add(6)
    s.add(7)
    s.add(8)
    s.add(9)
    s.add(10)
    s.add(11)
    s.add(12)
    s.add(13)
    s.add(14)
    s.add(15)
    s.add(16)
    s.add(17)
    s.add(18)
    s.add(19)
    s.add(20)
    s.add(21)
    print(s.test())
    s.pop(0)
    s.pop(1)
    s.pop(0)
    s.pop(2)
    s.pop(4)
    print(s.test())
    s.pop(5)
    print(s.test())

