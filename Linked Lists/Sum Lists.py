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

def sum_lists(l1, l2):
    carry = 0
    head = Node(0)
    current = head
    
    while l1 or l2 or carry:
        v1 = l1.value if l1 else 0
        v2 = l2.value if l2 else 0
        sum_value = v1 + v2 + carry
        carry = sum_value // 10
        current.next = Node(sum_value % 10)
        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return head.next

def main():
    l1 = Node(7)
    l1.next = Node(1)
    l1.next.next = Node(6)

    l2 = Node(5)
    l2.next = Node(9)
    l2.next.next = Node(2)

    result = sum_lists(l1, l2)
    print_list(result)

if __name__ == "__main__":
    main()