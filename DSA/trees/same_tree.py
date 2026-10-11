# You are given two binary trees, p and q.
# Return True if they have:
# - the same structure
# - the same values in the same places
# Example:
# Tree p:        Tree q:

#     1              1
#    / \            / \
#   2   3          2   3
# >>> True

# But
# Tree p:        Tree q:

#     1              1
#    /                \
#   2                  2
# >>> False
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')

root1=TreeNode('A')
root1.left = TreeNode('B')
root1.right = TreeNode('C')
# root1.left.left = TreeNode('D')

def same_tree(p, q):
    # your code
    if p is None and q is None:
        return True
    
    if p is None or q is None:
        return False
    
    if p.val != q.val:
        return False
    
    return same_tree(p.left, q.left) and same_tree(p.right, q.right)
    
print(same_tree(root2, root1))