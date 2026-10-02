from collections import deque

# process the request in the same order they arrive >>> fifo
requests = ["A", "B", "C", "D"]
from collections import deque

def process_requests(requests: list[str]) -> list[str]:
    queue = deque()
    # result = []

    # your code
    for request in requests:
      queue.append(request)
      
    while queue:
      queue.popleft()
    return list(queue)

print(process_requests(requests=requests))
