# Node class for a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Solution class with reverseList method
class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            next_node = current.next  # Store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to the current node
            current = next_node       # Move to the next node

        return prev  # prev is the new head

# Helper function to create a linked list from a list of values
def createLinkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print a linked list
def printList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Example usage
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]  # List of values
    head = createLinkedList(values)  # Create the linked list

    print("Original Linked List:")
    printList(head)

    s = Solution()
    reversed_head = s.reverseList(head)  # Reverse the linked list

    print("Reversed Linked List:")
    printList(reversed_head)

head=[1 ,2 ,3 ,4 ,5 ,6]
s= Solution()
print(s.reverseList(head))