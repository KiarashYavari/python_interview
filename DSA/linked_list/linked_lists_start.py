class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3

def linked_list_to_list(head):
    current = head
    result = []
    while current:
      result.append(current.val)
      current = current.next
    return result

print(linked_list_to_list(node1))

def reverse_linked_list(head):
      current = head
      previous = None
      while current:
        # reverse
        next_node = current.next
        current.next = previous
        # move current
        previous = current
        current = next_node
        
      return previous

node1 = reverse_linked_list(node1)

print(node1.val)
print(node1.next.val)
