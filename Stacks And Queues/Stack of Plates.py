class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, value):
        if len(self.stack) >= self.capacity:
            raise Exception("Stack is full")
        self.stack.append(value)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack.pop()

    def is_full(self):
        return len(self.stack) == self.capacity

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if len(self.stack) == 0:
            raise Exception("Stack is empty")
        return self.stack[-1]

class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = [Stack(capacity)]

    def push(self, value):
        last_stack = self.stacks[-1]
        if last_stack.is_full():
            new_stack = Stack(self.capacity)
            new_stack.push(value)
            self.stacks.append(new_stack)
        else:
            last_stack.push(value)

    def pop(self):
        last_stack = self.stacks[-1]
        value = last_stack.pop()
        if last_stack.is_empty() and len(self.stacks) > 1:
            self.stacks.pop()
        return value

    def pop_at(self, index):
        if index < 0 or index >= len(self.stacks):
            raise IndexError("Index out of range")
        stack = self.stacks[index]
        value = stack.pop()
        if stack.is_empty() and len(self.stacks) > 1:
            del self.stacks[index]
        return value

# Example usage:
stacks = SetOfStacks(3)
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)  # New stack is created here
stacks.push(5)
print(stacks.pop())      # Outputs: 5
print(stacks.pop_at(0))  # Outputs: 3
print(stacks.pop())      # Outputs: 4
print(stacks.pop())      # Outputs: 2
print(stacks.pop())      # Outputs: 1
