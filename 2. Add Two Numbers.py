

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

'''
Runtime
3
ms
Beats
65.00%
Memory
19.39
MB
Beats
40.61%
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]: 
        res = None
        up = 0
        while l1 and l2:
            sum = l1.val + l2.val + up
            n = (sum) % 10
            up = (sum) // 10
            res = ListNode(n, res)
            l1 = l1.next
            l2 = l2.next

        l = l1 or l2
        while l:
            n = (l.val + up) % 10
            up = (l.val + up) // 10
            res = ListNode(n, res)
            l = l.next
        if up:
            res = ListNode(up, res)

        # printList(res)
        # back to order
        r = None
        while res:
            r = ListNode(res.val, r)
            res = res.next
        # printList(r)

        return r


def buildList(l):
    if not l:
        return None
    root = None
    for i in l[::-1]:
        node = ListNode(i, root)
        root = node
    return root

def printList(l):
    i = l
    while i:
        print(f'{i.val}', end=' ')
        i = i.next
    print()


if __name__ == '__main__':
    s1 = [3,7]
    s2 = [9,2]
    # output: [2,0,1]

    # s1 = [0]
    # s2 = [0]

    # s1 = [9,9,9,9,9,9,9]
    # s2 = [9,9,9,9]

    l1 = buildList(s1)
    l2 = buildList(s2)

    # printList(l1)

    s = Solution()
    r = s.addTwoNumbers(l1, l2)

    printList(r)