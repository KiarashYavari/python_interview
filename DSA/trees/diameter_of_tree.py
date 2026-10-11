# The diameter is the longest path between any two nodes in the tree.
    #     A
    #    / \
    #   B   C
    #  / \
    # D   E
    # longest path could be:
    # D → B → A → C
    # That path has 3 edges, so the diameter is: 3
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

    #     1
    #    / \
    #   2   3
    #  / \ / \
    # 4  5 6  7

def diameter_of_binary_tree(root):
    diameter = 0

    def dfs(node):
        # base case
        nonlocal diameter
        if node is None:
            return 0
        
        # calculate left depth
        # calculate right depth
        left_diameter = dfs(node.left)
        right_diameter = dfs(node.right)
        
        # update diameter
        diameter = max(diameter, left_diameter + right_diameter)
        
        # return this node's depth
        return 1 + max(left_diameter, right_diameter)

    dfs(root)
    return diameter

print(diameter_of_binary_tree(root2))