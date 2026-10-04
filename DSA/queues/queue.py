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
#---------------------------------------------
# Return and remove the first customer in line.

customers = ["John", "Sara", "Mike", "Anna"]
# John
def serve_customer(customers: list[str]) -> str:
    queue = deque(customers)
    # your code
    return queue.popleft()
# --------------------------------------------
# Serve All Customers
def serve_customer(customers: list[str]) -> list[str]:
    queue = deque(customers)
    serve = []
    # your code
    while queue:
        customer = queue.popleft()
        serve.append(customer)
        
    return serve
        
    
