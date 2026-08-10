

from collections import deque
from typing import List, Optional

from treeUtils import TreeNode, buildTree

'''
使用BFS, 广度优先搜索左层次遍历
额外使用一个变量记录层数

生成结果的逻辑有些负责，有优化空间
'''
class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque()

        queue.append([root, 0])

        last_level = -1

        nodeList = None
        while queue:
            node, level = queue.popleft()
        
            if node != None:
                # print(node.val, level)
                if level == 0:
                    nodeList = [node.val]
                elif level != last_level:
                    res.append(nodeList)
                    nodeList = [node.val]
                else:
                    nodeList.append(node.val)
                last_level = level

                queue.append([node.left, level+1])
                queue.append([node.right, level+1])

        if nodeList:
            res.append(nodeList)

        return res

'''
对bfs做了优化
保存当前层和下一层Nodes
不断地将当前层的所有子树都放入下一层queue
之后将下一层作为当前层继续
'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        currentLevelQueue = deque()
        nextLevelQueue = deque()
        nextLevelQueue.append(root)

        while nextLevelQueue:
            currentLevelQueue = nextLevelQueue
            nextLevelQueue = deque()
            nodes = []
            while currentLevelQueue:
                node = currentLevelQueue.popleft()
                nodes.append(node.val)

                if node.left:
                    nextLevelQueue.append(node.left)
                if node.right:
                    nextLevelQueue.append(node.right)
            res.append(nodes)

        return res


if __name__ == '__main__':
    tree = buildTree([3,9,20,None,None,15,7])
    # preorderPrint(tree)

    s = Solution()
    print(s.levelOrder(tree))