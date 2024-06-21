class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def is_palindrome(head):
    if not head:
        return True
    
    slow = fast = head
    stack = []
    
    while fast and fast.next:
        stack.append(slow.value)
        slow = slow.next
        fast = fast.next.next
    
    if fast:
        slow = slow.next
    
    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next
    
    return True

def main():
    palindrome_head = Node(1)
    palindrome_head.next = Node(2)
    palindrome_head.next.next = Node(2)
    palindrome_head.next.next.next = Node(1)

    print(is_palindrome(palindrome_head))

if __name__ == "__main__":
    main()