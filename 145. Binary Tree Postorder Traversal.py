

from typing import List, Optional

from treeUtils import TreeNode, buildTree


'''
递归
'''
class Solution1:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(node):
            if node:
                postorder(node.left)
                postorder(node.right)
                res.append(node.val)

        postorder(root)
        return res


'''
非递归
关键在于增加一个processed flag来判断当前node是否已经处理完左右子树
* pop时，如果processed=False, 说明没处理过它的左右子树，那么该node重新入栈，
同时flag标记为True，其左右子树也入栈
* pop时，如果processed=True, 说明其左右子树已经处理完，此时输出node.val即可
'''
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = []
        stack.append([root, False])

        while stack:
            node, processed = stack.pop()

            if node:
                if processed:
                    res.append(node.val)
                    continue
                stack.append([node, True])
                stack.append([node.right, False])
                stack.append([node.left, False])

        return res


if __name__ == '__main__':
    tree = buildTree([1,2,3,4,5,None,8,None,None,6,7,9])
    # preorderPrint(tree)

    s = Solution()
    print(s.postorderTraversal(tree))