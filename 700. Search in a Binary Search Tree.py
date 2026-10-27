

from treeUtils import TreeNode, buildTree, showTree, showTreeSideways, showTreeSlash

'''
思路
直接遍历BST,搜索目标node即可
'''

class Solution:
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        def search(root):
            if root:
                if root.val == val:
                    return root
                elif root.val < val:
                    return search(root.right)
                else:
                    return search(root.left)
            return None

        return search(root)

if __name__ == '__main__':
    s = Solution()

    showTreeSlash(s.searchBST(buildTree([4,2,7,1,3]), 2))
    showTreeSlash(s.searchBST(buildTree([10,5,15,3,7,13,18,1,None,6]),10))
    showTreeSlash(s.searchBST(buildTree([4,2,7,1,3]), 5))
    # print(s.rangeSumBST(buildTree([10]), 9, 15))
    # print(s.rangeSumBST(buildTree([10]), 12, 15))