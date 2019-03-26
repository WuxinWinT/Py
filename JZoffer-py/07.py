# 007-斐波拉契数列

#题目描述：大家都知道斐波那契数列，现在要求输入一个整数n，
#请你输出斐波那契数列的第n项（从0开始，第0项为0）。 n<=39

#思路： f(n)=f(n-1)+f(n-2)

def Fibonacci(n):
    # write code here
    f1 = 0
    f2 = 1
    if n == 0: return f1
    elif n == 1: return f2
    for _ in range(n-1):
        f2, f1 = f1+f2, f2
    # f2 = f3(现值) = f1(初值) + f2(初值), f1（用于下一个） = f2(初值)
    # f2 = f4(现值) = f1 + f2 
    return f2
print(Fibonacci(4))
