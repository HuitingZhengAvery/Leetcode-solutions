# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def insertRight(root, node):
            if root.right is None:
                root.right = node
            else:
                insertRight(root.right, node)
                
        if root.val is None:
            return
        else:
            if root.left:
                if root.right is None:
                    root.right = root.left
                    root.left = None
                    self.flatten(root.right)
                else:
                    temp = root.right
                    root.right = root.left
                    root.left = None
                    insertRight(root, temp)
                    self.flatten(root.right)
            else:
                self.flatten(root.right)
                

            