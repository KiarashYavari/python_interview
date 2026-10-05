# Maximum Depth of Binary Tree?
#     A
#    / \
#   B   C
#  /
# D
# expected output >>> 3
# because the longest path from the root to a leaf is: A → B → D
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')

# max depth is the max depth between: left sub-tree and right sub-tree
def max_depth(root):
    def dfs(node):
        if node is None:
            return 0

        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        # +1 counts the current node   
        return 1 + max(left_depth, right_depth)
        
    max_depth = dfs(root)   
    return max_depth

print(max_depth(root2))
# if you trace it:
# D -> returns 1
# B -> returns 2
# A -> returns 3