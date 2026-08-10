

'''
思路一 有bug
递归的计算一个tree的左右子树，
如果左右子树都是BST，在判断当前tree是否满足BST
以上是第一感觉，但是有问题，BST要求左子树上所有node < 当前root，
以上方法有可能出现右子树自身是BST但是有node可能小于当前root

改进方式一
需要保存左子树上最大节点值，右子树最小节点值，用这两个值和root比较，
而不是简单的用子树的node值
难点在于怎么知道某个子树需要保存最大还是最小值？所以都保存

思路二
对BST中根遍历，应该是升序
但是能保证中根遍历升序的树一定是BST吗？

比如：
[5,4,6,null,null,3,7]
中序输出：4,5,3,6,7

让AI给出了证明：
若 inorder(T) 严格升序，则 T 是 BST。
'''

from typing import Optional

from treeUtils import TreeNode, buildTree

'''
思路一代码, 错误
有bug

反例：
[5,4,6,null,null,3,7]
应该false

'''
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(node):
            if not node:
                return True

            if node.left == None and node.right == None:
                return True # leaf node
            if node.left and node.right:
                if node.val > node.left.val and node.val < node.right.val:
                    return True and isBST(node.left) and isBST(node.right)
                return False
            if node.left:
                if node.val > node.left.val:
                    return True and isBST(node.left)
                return False
            if node.right:
                if node.val < node.right.val:
                    return True and isBST(node.right)
                return False

        return isBST(root)

'''
改进方式一代码实现
Accepted

有优化空间
'''
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isBST(node):
            if not node:
                return [True, None, None]

            if node.left == None and node.right == None:
                return [True, node.val, node.val] # leaf node
            
            elif node.left and node.right:
                lBST, lmin, lmax = isBST(node.left)
                rBST, rmin, rmax = isBST(node.right)
                if lBST and rBST:
                    if node.val > lmax and node.val < rmin:
                        return [True, lmin, rmax]
            elif node.left:
                lBST, lmin, lmax = isBST(node.left)
                if lBST and node.val > lmax:
                    return [True, lmin, node.val]
            elif node.right:
                rBST, rmin, rmax = isBST(node.right)
                if rBST and node.val < rmin:
                    return [True, node.val, rmax]
            
            return [False, None, None]

        return isBST(root)[0]  

'''
采用中序遍历方式
若 inorder(T) 严格升序，则 T 是 BST。

Accepted
''' 
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        res = []
        
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)

        for i in range(len(res) - 1): 
            if res[i+1] <= res[i]: # edge case: [2,2,2]
                return False
        return True


if __name__ == '__main__':
    tree = buildTree([5,4,6,None,None,3,7])
    # preorderPrint(tree)

    s = Solution()
    print(s.isValidBST(tree))