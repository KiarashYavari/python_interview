    #       A
    #      / \
    #     B   C
    #    / \
    #   D   E
# The lowest common ancestor of D and E is B.
# But the lowest common ancestor of D and C is A.

# Important rule
# A node can be an ancestor of itself.
# the lowest common ancestor of B and D is B
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')
root2.left.right = TreeNode('E')

def lowest_common_ancestor(root, p, q):

    def dfs(node):
        
        # Base case: empty node
        if node is None:
            return None
        print("node is ", node.val)
        # Base case: found p or q
        if node == p or node == q:
            return node
        
        # Search left and right subtrees
        left = dfs(node.left)
        right = dfs(node.right)

        # If both sides return a node,
        # the current node is the LCA
        if left and right:
            print("left: ", left.val)
            print("right: ", right.val)
            return node

        # Otherwise return whichever side
        # found a target
        return left or right

    return dfs(root)

print(lowest_common_ancestor(root2, root2.left.left, root2.left.right).val)