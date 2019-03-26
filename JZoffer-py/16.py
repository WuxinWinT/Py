# 016-合并有序链表
题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

思路

新开个链表，按大小存储即可

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(pHead1, pHead2):
    res = ListNode(0)
    pHead = res
    while pHead1 and pHead2:
        if pHead1.val >= pHead2.val:
            res.next = pHead2
            pHead2 = pHead2.next
        else:
            res.next = pHead1
            pHead1 = pHead1.next
        res = res.next
    if pHead1:
        res.next = pHead1
    if pHead2:
        res.next = pHead2
    return pHead.next

        
