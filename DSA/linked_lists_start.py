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
