class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def kth_to_last(head, k):
    if not head:
        return None
    
    slow = fast = head

    for i in range(k):
        if not fast:
            return None
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(3)

    print(kth_to_last(head, 2).value)

if __name__ == "__main__":
    main()