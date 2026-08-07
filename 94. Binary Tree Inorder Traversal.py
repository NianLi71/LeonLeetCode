
from typing import List, Optional

from treeUtils import TreeNode, buildTree, preorderPrint

'''
递归实现
'''
class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)

        inorder(root)
        return res

'''
非递归
关键点是，一个node要进出stack两次
第一次是和左右子树一起放回stack，并按照 right, node, left顺序进栈
第二次是左子树已经遍历完成，此时输出node节点即可

Runtime
0
ms
Beats
100.00%
Memory
19.20
MB
Beats
92.28%

'''
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        stack = [(root, 0)]
        while stack:
            node, time = stack.pop()
            
            if node:
                if time == 1:
                    res.append(node.val)
                else:
                    stack.append((node.right,0))
                    stack.append((node, time + 1))
                    stack.append((node.left, 0))

        return res
        

if __name__ == '__main__':
    tree = buildTree([1,2,3,4,5,None,8,None,None,6,7,9])
    # preorderPrint(tree)

    s = Solution()
    print(s.inorderTraversal(tree))