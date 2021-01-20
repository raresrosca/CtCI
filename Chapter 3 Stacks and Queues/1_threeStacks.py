class ThreeStack:
    def __init__(self, capacity = 5):
        capacity = capacity * 3 # since we have 3 stacks
        self.items = [None] * capacity
        # pointers for tops of stacks 0, 1, 2
        self.tops = [0, capacity // 3, 2 * (capacity // 3)]
        # pointers for limits of stacks 0, 1, 2
        self.limits = [capacity // 3, 2 * (capacity // 3), capacity]
  
    def push(self, stack, item):
        if stack > 2:
            raise ValueError("stack does not exist")
        
        if self.tops[stack] >= self.limits[stack]:
            raise Exception(f"stack {stack} is full")
        
        self.items[self.tops[stack]] = item
        self.tops[stack] += 1

    
    def pop(self, stack):
        if stack > 2:
            raise ValueError("stack does not exist")
        top = self.tops[stack] - 1
        if top < 0 or self.items[top] == None:
            raise IndexError("pop from empty stack")
        
        item = self.items[top]
        self.items[top] = None
        self.tops[stack] = top - 1

        return item