#     10
#    /  \
#   5    15
#  / \
# 3   7
# A tree is a data structure made of nodes connected in a hierarchy.
# Here:
# - 10 is the root
# - 5 and 15 are children of 10
# - 3 and 7 are children of 5
# - 3, 7, and 15 are leaf nodes because they have no children

# A binary tree means each node can have at most two children.
# left child
# right child
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = TreeNode(10)

root.left = TreeNode(5)
root.right = TreeNode(15)

root.left.left = TreeNode(3)
root.left.right = TreeNode(7)

    #     A
    #    / \
    #   B   C
    #  /
    # D
    
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')