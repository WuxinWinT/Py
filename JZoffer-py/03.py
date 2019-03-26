#003-从尾到头打印链表

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法1：用辅助栈存储   栈：先进后出
def printListFromTailToHead(listNode):
    stack = []
    result_array = []
    node_p = listNode
    while node_p:
        stack.append(node_p.val)  # append 增加
        node_p = node_p.next
    while stack:
        result_array.append(stack.pop(-1))
    return result_array

# list.pop(obj=list[-1])       //默认为 index=-1，删除最后一个列表值。
# 0：删除列表第一个值  2：列表第三个值

# 解法2：本身栈调用

result_array = []
def printListFromTailToHead(listNode):
    # write code here
    if listNode:
        printListFromTailToHead(listNode.next)  #递归，一直到最后一个值，然后从最后一个值开始输出
        result_array.append(listNode.val)
    return result_array
