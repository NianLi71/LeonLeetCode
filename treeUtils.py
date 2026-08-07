from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 这个函数是按照标准数组定义树
# parent: i
# left child: 2 * i, right child: 2 * i + 1 去构建的
# 和leetcode 上给出的格式不同
# leetcode上给出缩略表示
def buildTreeStandard(nodeList): # [3,9,20,null,null,15,7]
    limit = len(nodeList)

    def build(i):
        if i >= limit: return None

        left_i = (i+1) * 2 - 1 # actual index in list
        right_i = (i+1)* 2 + 1 - 1

        if nodeList[i]:
            return TreeNode(
                nodeList[i], 
                build(left_i),
                build(right_i)
            )
        else:
            return None
            
    return build(0)


'''
处理leetcode的缩略格式: [1,2,3,null,5,null,8,null,null,null,7,null,9]
不能用 2i+1 / 2i+2 的下标公式, 因为 null 节点不占用后续的孩子位置
改成层序遍历: 每弹出一个节点, 就按顺序认领接下来的两个位置作为左右孩子
null 只消耗位置, 不入队, 所以它不会再认领自己的孩子 —— 这就是缩略格式的关键
'''
def buildTree(nodeList):
    if not nodeList or nodeList[0] is None:
        return None

    root = TreeNode(nodeList[0])
    queue = deque([root])
    i = 1 # 下一个待认领的位置

    while queue and i < len(nodeList):
        node = queue.popleft()

        if nodeList[i] is not None: # 注意用 is not None, 值为0的节点也是合法节点
            node.left = TreeNode(nodeList[i])
            queue.append(node.left)
        i += 1

        if i < len(nodeList) and nodeList[i] is not None:
            node.right = TreeNode(nodeList[i])
            queue.append(node.right)
        i += 1

    return root


def preorderPrint(tree):
    if tree:
        print(tree.val)
        preorderPrint(tree.left)
        preorderPrint(tree.right)
        

def inorderPrint(tree):
    if tree:
        inorderPrint(tree.left)
        print(tree.val)
        inorderPrint(tree.right)

if __name__ == '__main__':
    # t = buildTree([3,9,20,None,None,15,7] )
    # t = buildTree([1,2,3] )
    t = buildTree([1,2,3,None,5,None,8,None,None,None,7,None,9])
    inorderPrint(t)