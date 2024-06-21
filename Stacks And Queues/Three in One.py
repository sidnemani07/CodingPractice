class ThreeInOne:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values = [0] * (stack_size * self.number_of_stacks)
        self.sizes = [0] * self.number_of_stacks
    
    def is_full(self, stack_num):
        return self.sizes[stack_num] == self.stack_capacity
    
    def is_empty(self, stack_num):
        return self.sizes[stack_num] == 0
    
    def index_of_top(self, stack_num):
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size - 1
    
    def push(self, stack_num, value):
        if self.is_full(stack_num):
            raise Exception("Stack is full")
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value
    
    def pop(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        top_index = self.index_of_top(stack_num)
        value = self.values[top_index]
        self.values[top_index] = 0
        self.sizes[stack_num] -= 1
        return value
    
    def peek(self, stack_num):
        if self.is_empty(stack_num):
            raise Exception("Stack is empty")
        return self.values[self.index_of_top(stack_num)]

# Example usage:
stack_size = 3
three_stacks = ThreeInOne(stack_size)
three_stacks.push(0, 1)
three_stacks.push(0, 2)
three_stacks.push(0, 3)
print(three_stacks.pop(0))  # Outputs: 3
print(three_stacks.peek(0)) # Outputs: 2
