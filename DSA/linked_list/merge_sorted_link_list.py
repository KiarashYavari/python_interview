class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# link list a
node1a = ListNode(10)
node2a = ListNode(20)
node3a = ListNode(30)

node1a.next = node2a
node2a.next = node3a


# link list b
node1b = ListNode(12)
node2b = ListNode(23)
node3b = ListNode(28)

node1b.next = node2b
node2b.next = node3b



def merge_two_lists(list1, list2):
    # your code
    current1 = list1
    current2 = list2

    dummy = ListNode()
    tail = dummy

    while current1 and current2:
        if current1.val <= current2.val:
            tail.next = current1
            current1 = current1.next
        else:
            tail.next = current2
            current2 = current2.next

        tail = tail.next

    # one of these may still have nodes
    if current1:
        tail.next = current1

    if current2:
        tail.next = current2

    return dummy.next
                
        
        
        
    return dummy.next

new_head = merge_two_lists(node1a, node1b)
itr = new_head
while itr:
    print(itr.val)
    itr = itr.next