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

def partition(head, x):
    if not head:
        return None
    
    left_dummy = Node(0)
    right_dummy = Node(0)
    left = left_dummy
    right = right_dummy
    
    current = head
    while current:
        if current.value < x:
            left.next = current
            left = left.next
        else:
            right.next = current
            right = right.next
        current = current.next
    
    right.next = None
    left.next = right_dummy.next
    
    return left_dummy.next

def main():
    head = Node(3)
    head.next = Node(5)
    head.next.next = Node(8)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(2)
    head.next.next.next.next.next.next = Node(1)

    print_list(partition(head, 5))
    
if __name__ == "__main__":
    main()