class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self._move_stack1_to_stack2_if_needed()
        return self.stack2.pop() if self.stack2 else None

    def peek(self):
        self._move_stack1_to_stack2_if_needed()
        return self.stack2[-1] if self.stack2 else None

    def empty(self):
        return not self.stack1 and not self.stack2

    def _move_stack1_to_stack2_if_needed(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

# Example usage:
queue = MyQueue()
queue.push(1)
queue.push(2)
print(queue.peek())  # returns 1
print(queue.pop())   # returns 1
print(queue.empty()) # returns False
