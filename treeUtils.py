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


'''
竖向显示, 根在顶部, 用 ┌─┴─┐ 连接父子
每个子树先递归排版成一个矩形块, 再把左右两块并排拼起来
所以宽度是按实际需要长出来的, 稀疏的树不会浪费横向空间
'''
def showTree(tree):
    if tree is None:
        print('<empty tree>')
        return
    lines, _, _ = _renderTopDown(tree)
    print('\n'.join(line.rstrip() for line in lines))


# 返回 (lines, width, root_col): 所有行等宽, root_col 是本块根标签中心所在的列
# slash=True 时连接线画成 / \, 否则画成 ┌─┴─┐, 排版逻辑两者共用
def _renderTopDown(node, slash=False):
    label = str(node.val)
    n = len(label)

    L, lw, lc = _renderTopDown(node.left, slash) if node.left is not None else ([], 0, 0)
    R, rw, rc = _renderTopDown(node.right, slash) if node.right is not None else ([], 0, 0)

    if not L and not R:
        return [label], n, n // 2

    GAP = 2 # 左右子块之间的最小间隔

    if L and R:
        cl, cr = lc, lw + GAP + rc # 两个孩子标签的中心列
        body_w = lw + GAP + rw
        h = max(len(L), len(R)) # 两块高度不同, 矮的补空行
        L = L + [''] * (h - len(L))
        R = R + [''] * (h - len(R))
        body = [a.ljust(lw) + ' ' * GAP + b.ljust(rw) for a, b in zip(L, R)]
        p = (cl + cr) // 2 # 父节点居中在两个孩子之间
    elif L:
        cl, cr = lc, None
        body_w = lw
        body = [a.ljust(lw) for a in L]
        p = cl + 2 # 只有左孩子, 父节点往右让 2 格
    else:
        cl, cr = None, rc
        body_w = rw
        body = [b.ljust(rw) for b in R]
        p = rc - 2

    start = p - n // 2 # 标签起始列, 使其中心落在 p
    shift = max(0, -start) # 顶出左边界就整体右移
    if shift:
        body = [' ' * shift + line for line in body]
        p += shift
        start += shift
        if cl is not None: cl += shift
        if cr is not None: cr += shift
    width = max(body_w + shift, start + n)

    conn = [' '] * width
    if slash: # 斜杠放在父与子的中点, 视觉上指向孩子
        if cl is not None: conn[(cl + p) // 2] = '/'
        if cr is not None: conn[(p + cr) // 2] = '\\'
    elif cl is not None and cr is not None:
        conn[cl], conn[cr] = '┌', '┐'
        for i in range(cl + 1, cr): conn[i] = '─'
        conn[p] = '┴'
    elif cl is not None:
        conn[cl], conn[p] = '┌', '┘'
        for i in range(cl + 1, p): conn[i] = '─'
    else:
        conn[p], conn[cr] = '└', '┐'
        for i in range(p + 1, cr): conn[i] = '─'

    lines = [(' ' * start + label).ljust(width), ''.join(conn)]
    lines += [line.ljust(width) for line in body]
    return lines, width, p


r'''
竖向显示, 用 / \ 画分支, 手写树的那种样子
排版和 showTree 完全一样, 只是把 ┌─┴─┐ 换成斜杠
'''
def showTreeSlash(tree):
    if tree is None:
        print('<empty tree>')
        return
    lines, _, _ = _renderTopDown(tree, slash=True)
    print('\n'.join(line.rstrip() for line in lines))


'''
横向显示, 根在左上角, 每深一层缩进一级
标注 L / R 是因为只有一个孩子时, 光看缩进分不出是左还是右
不管树多深都不会横向撑爆, 适合看退化成链的树
'''
def showTreeSideways(tree):
    if tree is None:
        print('<empty tree>')
        return

    out = [str(tree.val)]

    def walk(node, prefix):
        kids = [(c, tag) for c, tag in ((node.left, 'L'), (node.right, 'R')) if c is not None]
        for i, (child, tag) in enumerate(kids):
            last = i == len(kids) - 1
            out.append(prefix + ('└── ' if last else '├── ') + tag + ': ' + str(child.val))
            walk(child, prefix + ('    ' if last else '│   '))

    walk(tree, '')
    print('\n'.join(out))


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
    t = buildTree([5,2,2,4,None,None,1,None,1,None,4,2,None,2,None])
    showTree(t)
    print()
    showTreeSideways(t)
    print()
    showTreeSlash(t)