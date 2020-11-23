from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
解法：链表的插入排序
    - 时间复杂度：O(n^2)，n为链表长度
    - 空间复杂度：O(1)
"""
class Solution:
    def insertionSortList(self, head: ListNode) -> List[int]:
        if not head:
            return head
        
        dummyHead = ListNode(0) # 哑节点
        dummyHead.next = head   
        lastSorted = head       # 已排序部分的最后一个节点
        cur = head.next         # 待插入元素

        while cur:
            if lastSorted.val <= cur.val:    # 如果待插入元素最大就插在最后
                lastSorted = lastSorted.next
            else:                            # 否则从链表头节点遍历以寻找插入位置
                pre = dummyHead
                while pre.next.val <= cur.val:
                    pre = pre.next
                lastSorted.next = cur.next
                cur.next = pre.next
                pre.next = cur
            cur = lastSorted.next            # 处理下一个待插入元素

        return dummyHead.next                  

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
    head = listToListNode([4, 2, 1, 3])
    printListNode(Solution().insertionSortList(head)) 