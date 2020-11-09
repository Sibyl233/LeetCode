from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：双指针
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         pre, cur = None, head #定义指针
#         while cur:
#             cur.next, pre, cur = pre, cur, cur.next
#         return pre

# 解法2：递归
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(head == None or head.next == None): return head
        cur = self.reverseList(head.next)
        head.next.next = head #head的下一个节点指向head
        head.next = None
        return cur

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
    head = listToListNode([1, 2, 3, 4, 5, ])
    printListNode(Solution().reverseList(head))