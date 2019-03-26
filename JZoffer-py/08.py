# 008-跳台阶

#题目描述：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
#求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

#思路：假设对于第n级台阶，总共有f(n)种跳法.
#那么f(n) = f(n-1) + f(n-2)，其中f(1)=1,f(2)=2 （与007一样）

def jumpFloor(number):
    f1 = 1
    f2 = 2
    if number == 1:
        return f1
    if number == 2:
        return f2
    for _ in range(number - 2):
        f2 , f1 = f1 + f2 , f2
    return f2

print(jumpFloor(4))

    