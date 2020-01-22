def insert(self, x):
    if self.val:
        if self.left is None:
            self.left = TreeNode(x)
        else:
            self.right.insert(x)
    else:
        self.val = x
