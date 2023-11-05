class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    first = cur = head
    last = None
    
    while first != last:
        while cur.next != last:
            cur = cur.next
        last = cur
        if first.val != last.val:
            return False
        first = cur = first.next
    return True
node = ListNode(1)
print(isPalindrome(node))