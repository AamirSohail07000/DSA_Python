# Given the head of a singly linked list, reverse the list, and return the reversed list's new head

# Definition for a singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode) -> ListNode:
    """
    Reverses a singly linked list iteratively.
    """
    prev = None
    current = head
    while current:
        next_node = current.next  # 1. Store the next node
        current.next = prev       # 2. Reverse the current node's pointer
        prev = current            # 3. Move 'prev' to the current node
        current = next_node       # 4. Move 'current' to the next node
    return prev

# Helper function to convert list to linked list
def list_to_linkedlist(arr):
    if not arr: return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print linked list
def print_linkedlist(head):
    nodes = []
    current = head
    while current:
        nodes.append(str(current.val))
        current = current.next
    return " -> ".join(nodes)

# Example Usage:
print("\n--- Reverse Linked List ---")
list1 = list_to_linkedlist([1, 2, 3, 4, 5])
reversed_list1 = reverse_list(list1)
print(f"Reversed List: {print_linkedlist(reversed_list1)}")  