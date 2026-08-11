

'''
思路一
直接同步遍历两棵树， 如果节点不一致就不是same tree
任意遍历方式都可以
'''


from typing import Optional

from treeUtils import TreeNode, buildTree

'''
思路一实现
同时先序遍历两棵树
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        def inorder(p, q):
            nonlocal same
            if not same:
                return
            if (p and not q) or (not p and q):
                same = False
                return
            if p and q:
                inorder(p.left, q.left)
                if p.val != q.val:
                    same = False
                    return
                inorder(p.right, q.right)

        inorder(p, q)

        return same

'''
思路二
递归的去判断左右子树是否是sameTree

Accepted
'''
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if (not p and q) or (p and not q):
            return False
        elif not p and not q:
            return True
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right);


if __name__ == '__main__':

    s = Solution()
    print(s.isSameTree(buildTree([]), buildTree([])))
    print(s.isSameTree(buildTree([1,2,1]), buildTree([1,1,2])))