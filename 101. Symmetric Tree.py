

'''
思路一
同步遍历根节点的左右子树，但是每次：
1.根节点左子树向左遍历，根节点的右子树就向左遍历
2.根节点左子树向右遍历，根节点的右子树就向左遍历


思路二：
非递归实现

思路三
如果对根节点左子树做：中序遍历
对根节点的右子树做：右->中->左 遍历
之后比较遍历顺序？有反例？
'''


from typing import Optional

from treeUtils import TreeNode, buildTree


'''
思路一实现
递归

Accepted
'''
class Solution1:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isMirror(l, r):
            if not l and r or l and not r:
                return False
            if not l and not r:
                return True
            if l.val != r.val:
                return False
            
            return isMirror(l.left, r.right) and isMirror(l.right, r.left)

        return isMirror(root.left, root.right)


'''
思路二：
非递归实现

Accepted
'''
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        s = []
        s.append([root.left, root.right])
        while s:
            l, r = s.pop()

            if not l and r or l and not r:
                return False
            if not l and not r:
                continue # never return True here!
            if l.val != r.val:
                return False

            s.append([l.left, r.right])
            s.append([l.right, r.left])

            # 不需要处理递归中: isMirror(l.left, r.right) and isMirror(l.right, r.left)
            # 非递归中如果两个其中一个是False，isSymmetric就直接return了

        return True




if __name__ == '__main__':

    s = Solution()
    print(s.isSymmetric(buildTree([5,2,2,4,None,None,1,None,1,None,4,2,None,2,None])))
    print(s.isSymmetric(buildTree([2,1,1])))
    print(s.isSymmetric(buildTree([1,2,2,None,3,None,3])))
    print(s.isSymmetric(buildTree([1,2,2,3,4,4,3])))