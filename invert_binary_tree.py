# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         return invertTree(root)

def invertTree(root):
#   if root == None:
#       return None
    if not root: return

    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root

class Solution:
    def invertTree(self, root):
        return invertTree(root)

# class Solution:
#     def invertTree(self, root):
#         if not root: return
#         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
#         return root