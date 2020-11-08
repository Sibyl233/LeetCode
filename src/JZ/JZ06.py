from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：用栈实现
# class Solution:
#     def reversePrint(self, head: ListNode) -> List[int]:
#         stack = []
#         while head:
#             stack.append(head.val)
#             head = head.next
#         return stack[::-1]

# 解法2：递归
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        return self.reversePrint(head.next) + [head.val] if head else []



def listToListNode(list):
    head = ListNode(list[0])
    p = head
    for i in range(1, len(list)):
        p.next = ListNode(list[i])
        p = p.next
    return head

if __name__=="__main__": 
    head = listToListNode([1, 3, 2])
    print(Solution().reversePrint(head)) # [2, 3, 1]