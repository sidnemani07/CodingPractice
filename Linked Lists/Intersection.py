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

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def get_intersection_node(headA, headB):
    lenA = get_length(headA)
    lenB = get_length(headB)
    
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    
    while lenB > lenA:
        headB = headB.next
        lenB -= 1
    
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    
    return None

def main():
    headA = Node(1)
    headA.next = Node(2)
    headA.next.next = Node(2)
    headA.next.next.next = Node(3)

    headB = Node(0)
    headB.next = Node(2)
    headB.next.next = Node(4)
    headB.next.next.next = Node(5)

    print(get_intersection_node(headA, headB))

if __name__ == "__main__":
    main()