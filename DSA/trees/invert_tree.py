class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root2=TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)

def invert_tree(root):
    # your code
    if root:
        root.left, root.right = root.right, root.left
        invert_tree(root.left)
        invert_tree(root.right)
        
    return root

invert_tree(root=root2)
# def print_tree(root):
#     if root:
#         print(root.val)
#         print_tree(root.left)
#         print_tree(root.right)
# print_tree(root=root2)