class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def findWords(head, k):
    cur = head
    lenList = 0
    while cur:
        lenList += 1
        cur = cur.next
    groups = lenList // k
    cur = head
    for i in range(groups):
        cur2 = cur
        pre = None
        for j in range(k):
            tmp = cur2.next
            cur2.next = pre
            pre = cur2
            cur2 = tmp
        cur.next = cur2
        cur = cur2
        if i == 0:
            head = pre
    return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print(findWords(head, 2)) 