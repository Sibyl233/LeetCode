from utils.listNode import *

"""解法：
- 时间复杂度：O(n)
- 空间复杂度：O(1)
"""
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

if __name__=="__main__": 
    head = listToListNode([1,2,3,4,5, ])
    printListNode(Solution().oddEvenList(head))   