# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        former, latter = head, head #初始化：前、后节点都指向头结点
        for _ in range(k):          #构建双指针距离：前节点先走k步
            if not former: return   #考虑k大于链表长度的情况
            former = former.next
        while former:               #双指针共同移动：当前节点走过尾节点时后节点恰好处于倒数第k个节点
            former, latter = former.next, latter.next
        return latter

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
    head = listToListNode([1,2,3,4,5])
    k = 2
    printListNode(Solution().getKthFromEnd(head, k))