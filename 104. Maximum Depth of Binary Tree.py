# Tree


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from treeUtils import TreeNode, buildTree



'''
Runtime
0
ms
Beats
100.00%
Memory
22.63
MB
Beats
14.49%
'''
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxD = 0
        def dfs(d, node):
            nonlocal maxD
            if not node: return
            if d > maxD:
                maxD = d
            dfs(d+1, node.left)
            dfs(d+1, node.right)

        dfs(1, root)

        return maxD

'''
优化版递归比较左右子树深度
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(d, node):
            if not node: return d
            d += 1
            return max(dfs(d, node.left), dfs(d, node.right))

        return dfs(0, root)

if __name__ == '__main__':
    tree = buildTree([3,9,20,None,None,15,7])
    # tree = buildTree([])
    s = Solution()
    print(s.maxDepth(tree))