# Merge K Sorted Lists
# This is our final topic in the Heaps & Priority Queues roadmap.
# Problem: LeetCode 23 — Merge K Sorted Lists
# You're given k sorted linked lists. Merge them into one sorted linked list.

# For example:
# list1 = 1 -> 4 -> 5
# list2 = 1 -> 3 -> 4
# list3 = 2 -> 6

# expected results: 1 -> 1 -> 2 -> 3 -> 4 -> 4 -> 5 -> 6
# Each linked list is already sorted. Therefore, we only need to compare the first available node from each list.

import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node4.next = node5
node5.next = node6


def merge_k_lists(lists: list[ListNode]) -> ListNode:
    heap = []

    # Step 1: Push the first node of
    # every non-empty list into the heap
    for i ,l_list in enumerate(lists):
      if l_list:
        heapq.heappush(heap, (l_list.val, i, l_list))

    dummy = ListNode(0)
    current = dummy

    # Step 2: While the heap isn't empty:
    while heap:
      # - Pop smallest node
      node_val, index, node = heapq.heappop(heap)
      # print(f"popped node is: {node_val}, {index}")
      # - Attach it to current.next
      current.next = node
      # - Move current forward
      current = current.next
      # - Push popped node's next, if any
      if current.next:
        heapq.heappush(heap, (current.next.val, index, current.next))

    return dummy.next
  
def print_linked_list(head):
    values = []

    while head:
        values.append(head.val)
        head = head.next

    print(" → ".join(map(str, values)))


result = merge_k_lists([node1, node4])

print_linked_list(result)