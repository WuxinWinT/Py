# 009-变态跳台阶

#题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
#求该青蛙跳上一个n级的台阶总共有多少种跳法。

#思路：f(1)=1, f(2)=2, f(3)=4, f(4)=8 设n+1级f(n+1),有
# f(n+1) = f(1) + f(2) + ... + f(n)
# f(n+2) = f(1) + f(2) + ... + f(n+1)
# f(n+2)= 2f(1) + 2f(2) + ... + 2f(n)
# 故得f(n+2) = 2f(n+1)

def jumpFloorII(number):
    f1 = 1
    if number == 1:
        return f1
    for _ in range(number-1):
        f1 = 2 * f1   # f2 = 2 * f1 为错误，因为f2无法被赋值
    return f1
