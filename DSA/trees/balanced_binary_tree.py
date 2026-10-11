# Balanced Binary Tree
# same recursive depth calculation
# the left and right subtree heights cannot differ by more than 1 at any node
# A binary tree is height-balanced if, for every node, the heights of its left and right subtrees differ by at most 1.
# Mathematically:
#   |left_height - right_height| <= 1
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')
# root2.left.left.left = TreeNode('E')

    #       A
    #      / \
    #     B   C
    #    /
    #   D
    #  / 
    # E

# Key takeaway: We must check the balance condition at every node.
def is_balanced(root):
    # Your implementation
    balanced = True
    def dfs(node):
        nonlocal balanced
        if node is None:
            return 0
        
        left_depth = dfs(node.left)
        right_depth = dfs(node.right)
        if abs(left_depth - right_depth) > 1:
            balanced = False
        return 1+ max(left_depth, right_depth)
    
    dfs(root) 
    return balanced
        
print(is_balanced(root2))