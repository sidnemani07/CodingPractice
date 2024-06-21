def sort_stack(stack):
    temp_stack = []

    while stack:
        tmp = stack.pop()
        while temp_stack and temp_stack[-1] > tmp:
            stack.append(temp_stack.pop())
        temp_stack.append(tmp)

    while temp_stack:
        stack.append(temp_stack.pop())

# Example usage:
stack = [34, 3, 31, 98, 92, 23]
sort_stack(stack)
print(stack)  # Output: [3, 23, 31, 34, 92, 98]
