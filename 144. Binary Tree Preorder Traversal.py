

from typing import List, Optional

from treeUtils import TreeNode, buildTree


class Solution1:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return res


'''
非递归
'''
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()

            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return res


if __name__ == '__main__':
    tree = buildTree([1,2,3,4,5,None,8,None,None,6,7,9])
    # preorderPrint(tree)

    s = Solution()
    print(s.preorderTraversal(tree))