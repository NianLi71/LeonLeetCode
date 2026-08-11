
from typing import Optional

from listNodeUtils import *

'''
LinkList模拟操作
考虑remove head边界情况

Accepted
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def listLen(l):
            if not l: return 0
            p = l
            i = 0
            while p:
                i += 1
                p = p.next
            return i

        lLen = listLen(head)
        move = lLen - n

        if move > 0: # not remove head
            p = head
            i = 0
            while True:
                if i == move -1: break
                i += 1
                p = p.next
            p.next = p.next.next
        else: # remove head
            return head.next

        return head
        

if __name__ == '__main__':
    s = Solution()
    l = buildList([1,2,3,4,5])
    printList(l)
    newl = s.removeNthFromEnd(l, 1)
    printList(newl)

    l = buildList([1])
    printList(l)
    newl = s.removeNthFromEnd(l, 1)
    printList(newl)