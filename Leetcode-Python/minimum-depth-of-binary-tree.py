# Beats 93% of solutions -- Improvements suggested

class Solution:
    def __init__(self):
        self.result = None

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ld = self.findDepth(root.left)
        rd = self.findDepth(root.right)
        if ld and not rd:
            return ld
        elif rd and not ld:
            return rd
        elif not ld and not rd:
            return 1
        else:
            return min(ld, rd)

    def findDepth(self, main_node):
        if not main_node:
            return 0
        self.result = list()
        self.dfs_traverse([main_node])
        return len(self.result) + 1

    def dfs_traverse(self, arr):
        flag = False
        k = list()
        node_list = list()
        for node in arr:
            k.append(node.val)
            if node.left:
                node_list.append(node.left)
            if node.right:
                node_list.append(node.right)
            if not node.left and not node.right:
                flag = True
                break
        if len(k):
            self.result.append(k)
        if flag:
            return
        if len(node_list):
            self.dfs_traverse(node_list)