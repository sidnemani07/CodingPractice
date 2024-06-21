class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_middle_node(node):
    if node is None or node.next is None:
        return False
    
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next
    return True

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

    middle_node = head.next  # node with value 2
    delete_middle_node(middle_node)
    print_list(head)

if __name__ == "__main__":
    main()