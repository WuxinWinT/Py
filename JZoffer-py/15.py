# 015-反转链表
#输入一个链表，反转链表后，输出新链表的表头。

# 思路：
假设翻转1->2->3->4->5，步骤如下：

head->4->3->2->1->5
               p  tp

1.我们将p的next指向tp的next
2.将tp的next指向head的next
3.将head的next指向tp


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    if not pHead:return None
    head = ListNode(0)   # @不要忘记写！
    head.next = pHead
    p = pHead
    while(p.next): 
        tp = p.next
        p.next = p.next.next #思路的步骤1
        tp.next = head.next  #2
        head.next = tp       #3
    return head.next
