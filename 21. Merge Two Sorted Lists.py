# Definition for singly-linked list.
from typing import Optional

from listNodeUtils import ListNode, buildList, printList


'''
没有优化，新建Node
'''
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root = None
        while list1 and list2:
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            root = ListNode(val, root)

        listLeft = list1 or list2
        while listLeft:
            val = listLeft.val
            root = ListNode(val, root)
            listLeft = listLeft.next

        #reverse
        r = None
        while root:
            r = ListNode(root.val, r)
            root = root.next

        return r


class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = None
        while list1 and list2:
            if list1.val <= list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next

            node = ListNode(val, node)

            if not head:
                head = p = node
            else:
                p.next = node # 优化多加一个指针p
                p = node

        p.next = list1 or list2

        return head

'''
不新建Node
'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None

        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val <= list2.val:
            head=list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        p = head
        while list1 and list2:
            if list1.val <= list2.val:
                p.next = list1
                p = list1
                list1 = list1.next
            else:
                p.next = list2
                p = list2
                list2 = list2.next

        p.next = list1 or list2

        return head


if __name__ == '__main__':
    s1 = [3, 7, 10]
    s2 = [2, 9]
    # output: [2,0,1]

    # s1 = [0]
    # s2 = [0]

    # s1 = [9,9,9,9,9,9,9]
    # s2 = [9,9,9,9]

    l1 = buildList(s1)
    l2 = buildList(s2)

    s = Solution()
    printList(s.mergeTwoLists(l1, l2))
        
    # printList(l1)
    # printList(reverseList(l1))