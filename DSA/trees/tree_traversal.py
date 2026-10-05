# write a function called preorder_traversal(root) that returns a list instead of printing.
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
#     A
#    / \
#   B   C
#  /
# D   
root2=TreeNode('A')
root2.left = TreeNode('B')
root2.right = TreeNode('C')
root2.left.left = TreeNode('D')

def preorder(node):
    result = []

    def dfs(node):
        if node is None:
            return

        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(node)
    return result
    
# print(preorder(root2))
#----------------------------
# Inorder traversal > Left → Node → Right
# For the same tree, expected output is: ["D", "B", "A", "C"]
def inorder(node):
    result = []
    
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(node)
    return result
    
# print(inorder(root2))
#--------------------------------
# postorder: Left → Right → Node
# ["D", "B", "C", "A"]
def postorder(node):
    result = []
    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.val)
    dfs(node)
    return result
print(postorder(root2))