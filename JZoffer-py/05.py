# 005-用两个栈实现队列
#题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
#思路：一个栈用来存储 pop时弹出stack2，stack2为空，pop出stack1存储在stack2中
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

def push(self,node):
    self.stack1.append(node)

def pop(self):
    if not self.stack2:  # stack2为空
        while self.stack1:
            self.stack2.append(self.stack1.pop(-1))  #stack1 pop到 stack2
    return self.stack2.pop(-1)

#（来回倒腾）因为两次先进后出，则变成 先进先出
            
