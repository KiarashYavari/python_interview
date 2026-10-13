class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
      
root = TreeNode(8)

root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
#     8
#    / \
#   3   10
#  / \
# 1   6
def kth_smallest(root, k):
    # Your implementation
    result = []
    def inorder_dfs(node):
      if node is None:
        return None
      inorder_dfs(node.left)
      result.append(node.val)
      inorder_dfs(node.right)
    inorder_dfs(root)
    if k < len(result)+1:
      return result[k-1]
    return None

print(kth_smallest(root, 1))
