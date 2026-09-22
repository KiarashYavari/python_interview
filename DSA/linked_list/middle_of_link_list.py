class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(12)
node5 = ListNode(37)


node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
           
print(middle_node(node1).val)           
        