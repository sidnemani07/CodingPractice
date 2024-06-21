class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_duplicates(head):
    if not head:
        return head
    
    seen = set()
    current = head
    seen.add(current.value)

    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return head

def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)

    print_list(head)
    remove_duplicates(head)
    print_list(head)

if __name__ == "__main__":
    main()