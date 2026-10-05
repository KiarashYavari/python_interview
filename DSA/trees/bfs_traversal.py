#     A
#    / \
#   B   C
#  /
# D
# For BFS / level-order traversal, we visit the tree one level at a time.
# BFS order: A → B → C → D
# We use a queue
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')



def level_order(root):
    if root is None:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        
        result.append(node.val)
        
        # don't want to add None values to the queue    
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
            
    return result

print(level_order(root2))