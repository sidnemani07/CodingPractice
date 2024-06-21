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

def detect_cycle(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    
    if not fast or not fast.next:
        return None
    
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

def main():
    # Create a list with a cycle
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    
    # Creating a cycle: node with value 5 points to node with value 3
    head.next.next.next.next.next = head.next.next

    # Print list up to a certain number of nodes to visualize the cycle
    print("List with a cycle:")
    print_list(head)

    # Detect the cycle
    cycle_node = detect_cycle(head)
    if cycle_node:
        print(f"Cycle detected at node with value: {cycle_node.value}")
    else:
        print("No cycle detected")

if __name__ == "__main__":
    main()