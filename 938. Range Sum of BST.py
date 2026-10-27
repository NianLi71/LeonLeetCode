
'''
思路一
中序遍历BST，然后计算[low,high]之间的sum
注意low,high不一定在BST中

'''

from treeUtils import TreeNode, buildTree


class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        res = []
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        
        # print(res)
        sum = 0
        for e in res:
            if e < low:
                continue
            elif e > high:
                break
            else:
                sum += e
        
        return sum

'''
思路二
递归遍历左右子树，统计node.val在[low,high]内的sum
'''

class Solution2:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        if not root:
            return 0

        sum = self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        if root.val >= low and root.val <= high:
            sum += root.val

        return sum

if __name__ == '__main__':
    s = Solution2()

    print(s.rangeSumBST(buildTree([10,5,15,3,7,13,18,1,None,6]), 6, 10))
    print(s.rangeSumBST(buildTree([10,5,15,3,7,None,18]), 7, 15))
    print(s.rangeSumBST(buildTree([10]), 9, 15))
    print(s.rangeSumBST(buildTree([10]), 12, 15))