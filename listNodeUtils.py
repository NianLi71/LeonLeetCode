
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def reverseList(root):
    newRoot = None
    def reverse(r):
        if not r.next:
            nonlocal newRoot
            newRoot = r
            return r
        
        nr = reverse(r.next)
        nr.next = r
        return r

    root = reverse(root)
    root.next = None
    return newRoot