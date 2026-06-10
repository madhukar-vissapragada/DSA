# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.traverse(root, output)
        return output 
    

    def traverse(self, root: Optional[TreeNode], output: List[int]):
        if root:
            output.append(root.val)
            self.traverse(root.left, output)
            self.traverse(root.right, output)