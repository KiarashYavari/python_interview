class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)

node1.next = node2
node2.next = node3
node3.next = node1

def has_cycle(head):
    slow = head
    fast = head
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        count += 1
        # print(f"iteration {count}")
        # print(f"slow={slow.val}")
        # print(f"fast={fast.val}")
        # print("----------------")
        if slow == fast:
            return True
        
    return False

print(has_cycle(node1))