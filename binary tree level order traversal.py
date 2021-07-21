# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

def dfs(root, depth, result):
    if root == None:
        return
    print(depth, ":", root.val)
    
    if depth == len(result):
        result.append([])
        
    result[depth].append(root.val)
    
    dfs(root.left, depth+1, result)
    dfs(root.right, depth+1, result)

class Solution:
    def levelOrderBottom(self, root):
        result = []
        dfs(root, 0, result)
        result.reverse()
        return result