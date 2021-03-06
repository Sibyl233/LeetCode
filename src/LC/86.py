from utils.listNode import *

"""解法1：维护两个列表
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next

if __name__=="__main__": 
    head = listToListNode([1,4,3,2,5,2]) 
    x = 3
    printListNode(Solution().partition(head, x)) # 1->2->2->4->3->5