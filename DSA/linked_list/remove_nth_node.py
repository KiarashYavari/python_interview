class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node4 = ListNode(31)

node1.next = node2
node2.next = node3
node3.next = node4

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)

    slow = dummy
    fast = dummy

    # Phase 1:
    # move fast ahead n + 1 times
    for i in range(n+1):
        fast = fast.next

    # Phase 2:
    # move both together
    while fast:
        slow = slow.next
        fast = fast.next

    # Remove node
    slow.next = slow.next.next

    return dummy.next

new_head = remove_nth_from_end(node1, 3)
itr = new_head
while itr:
    print(itr.val)
    itr = itr.next
