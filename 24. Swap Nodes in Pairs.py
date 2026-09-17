


from listNodeUtils import ListNode, buildList, printList


'''
链表模拟题，
画图模拟指针移动位置，找出固定pattern重复即可
'''
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None: # 0 or 1 node
            return head

        q = head
        p = head.next

        # swap first pair
        q.next = p.next
        p.next = q
        head = p
        curTail = q # 当前的结尾node

        while q.next != None:
            q = q.next
            if q.next == None: # only one node left, can not swap
                break
            p = p.next.next.next

            # 重复swap 操作
            q.next = p.next
            p.next = q
            curTail.next = p
            curTail = q

        return head


if __name__ == '__main__':
    s = Solution()

    l = buildList([1,2,3,4,5])
    printList(l)
    newl = s.swapPairs(l)
    printList(newl)

    l = buildList([])
    printList(l)
    newl = s.swapPairs(l)
    printList(newl)

    l = buildList([1])
    printList(l)
    newl = s.swapPairs(l)
    printList(newl)

    l = buildList([1,2,3])
    printList(l)
    newl = s.swapPairs(l)
    printList(newl)