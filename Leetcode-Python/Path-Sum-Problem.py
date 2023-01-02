# Beats 98.4 perecent solutions - Recursive approach

class Solution:
    def __init__(self):
        self.flag = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, path_sum=0) -> bool:
        if not root:
            return False
        path_sum += root.val
        if root.left or root.right:
            if root.left:
                self.hasPathSum(root.left, targetSum, path_sum)
                if self.flag:
                    return True
            if root.right:
                self.hasPathSum(root.right, targetSum, path_sum)
                if self.flag:
                    return True
        else:
            if path_sum == targetSum:
                self.flag = True
        return self.flag
