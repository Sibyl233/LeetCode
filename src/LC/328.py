# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        evenHead = head.next # 为什么要有这一行
        odd, even = head, evenHead
        while even and even.next: # 为什么
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenHead
        return head

def listToListNode(list):
    head = ListNode(list[0])
    p = head
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return head

def printListNode(ListNode):
    p = ListNode
    while p != None:
        print(p.val, '->', end='')
        p = p.next
    print('NULL')

if __name__=="__main__": 
    head = listToListNode([1,2,3,4,5, ])
    printListNode(Solution().oddEvenList(head))   