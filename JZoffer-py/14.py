# 014-链表中倒数第k个结点

#思路:用快慢指针�，快指针比慢指针快k步，到尾结点了慢指针就是倒数第k个结点。
#eg:倒数第一个：为最后一个，so 倒数第k个，快针是先走k-1（而不是先走k）

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        #设置两个指针，p2指针先走（k-1）步，
        #然后再一起走，当p2为最后一个时，p1就为倒数第k个数
    
        p2=head
        p1=head
        #p2先走，走k-1步，如果k大于链表长度则返回 空，否则的话继续走
        while k>1:
            if p2.next!=None:
                p2=p2.next
                k-=1
            else:
                return None
        #两个指针一起 走，一直到p2为最后一个,p1即为所求
        while p2.next!=None:
            p1=p1.next
            p2=p2.next
        return p1
