class StackMin:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []
    
    def push(self, value):
        self.main_stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if not self.main_stack:
            raise Exception("Stack is empty")
        value = self.main_stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value
    
    def min(self):
        if not self.min_stack:
            raise Exception("Stack is empty")
        return self.min_stack[-1]
    
    def peek(self):
        if not self.main_stack:
            raise Exception("Stack is empty")
        return self.main_stack[-1]

# Example usage:
stack_min = StackMin()
stack_min.push(5)
stack_min.push(3)
stack_min.push(7)
stack_min.push(3)
print(stack_min.min())  # Outputs: 3
stack_min.pop()
print(stack_min.min())  # Outputs: 3
stack_min.pop()
print(stack_min.min())  # Outputs: 3
stack_min.pop()
print(stack_min.min())  # Outputs: 5
