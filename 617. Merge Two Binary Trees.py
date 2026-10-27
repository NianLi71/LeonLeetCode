



from treeUtils import TreeNode, buildTree, showTreeSlash


'''
思路一
merge root1 into root2
合并都有的node
在root2子树上link root1子树

注意root1,root2可以为空！
思路一要求root2不能为空
处理边界case

思路二
不要合并了， 新建一个tree，把r1 r2 merge到new tree中
一边遍历r1 r2, 一边递归创建新tree
对每个node递归merge左右子树
'''

'''
思路一实现
Accepted
'''
class Solution:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
        # 注意边界情况
        if not root1: return root2
        if not root2: return root1

        def merge(r1, r2):
            if r1 and r2:
                r2.val = r1.val + r2.val

                # 如果r1.left为空，就不在处理r2.left，不管r2.left是否为空
                # 同理对于r1.right为空时也一样
                # 因为我们是把r1 merge into r2, 所以只处理r1 left right非空情况
                if r1.left:
                    if r2.left:
                        merge(r1.left, r2.left)
                    else:
                        r2.left = r1.left
                if r1.right:
                    if r2.right:
                        merge(r1.right, r2.right)
                    else:
                        r2.right = r1.right
            
        merge(root1, root2)

        return root2

'''
思路二实现
'''
class Solution2:
    def mergeTrees(self, root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:

        def merge(r1, r2):
            newNode = TreeNode()

            if r1 and r2:
                newNode.val = r1.val+r2.val
                newNode.left = merge(r1.left, r2.left)
                newNode.right = merge(r1.right, r2.right)
            elif r1:
                newNode.val = r1.val
                newNode.left = r1.left
                newNode.right = r1.right
            elif r2:
                newNode.val = r2.val
                newNode.left = r2.left
                newNode.right = r2.right
            else:
                return None
            return newNode

        return merge(root1, root2)



if __name__ == '__main__':
    s = Solution2()

    showTreeSlash(s.mergeTrees(buildTree([1,3,2,5]), buildTree([2,1,3,None,4, None,7])))
    showTreeSlash(s.mergeTrees(buildTree([1]), buildTree([1,2])))
    showTreeSlash(s.mergeTrees(buildTree([]), buildTree([1,2])))
    showTreeSlash(s.mergeTrees(buildTree([1,2]), buildTree([])))
    # showTreeSlash(s.mergeTrees(buildTree([10,5,15,3,7,13,18,1,None,6]),10))
    # showTreeSlash(s.mergeTrees(buildTree([4,2,7,1,3]), 5))
    # print(s.rangeSumBST(buildTree([10]), 9, 15))
    # print(s.rangeSumBST(buildTree([10]), 12, 15))