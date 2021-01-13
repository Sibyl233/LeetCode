from utils.listNode import *

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next

if __name__=="__main__": 
    l1 = listToListNode([1,2,4])
    l2 = listToListNode([1,3,4])
    printListNode(Solution().mergeTwoLists(l1, l2))