class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

#     8
#    / \
#   3   10
#  / \
# 1   6
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

def insert_into_bst(root, val):
    # Your implementation
    if root is None:
        return TreeNode(val)
    if val > root.val:
        root.right = insert_into_bst(root.right, val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    
    return root
