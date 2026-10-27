'''
思路一
前序中序后序遍历整个树，如果有node 和root val不一样，就false

思路二
递归遍历左右子树，分解为子问题，左右子树是否是univalued binary tree
'''

from treeUtils import TreeNode, buildTree


class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        res = []
        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)
        preorder(root)

        for i in range(len(res)):
            if res[i] != res[0]:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUnivalTree(buildTree([2,2,2,5,2])))
    print(s.isUnivalTree(buildTree([1,1,1,1,1,None,1])))
    print(s.isUnivalTree(buildTree([1])))