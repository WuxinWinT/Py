# 010-矩形覆盖

# 题目描述：我们可以用 2 * 1 的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2 * 1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

#思路
# f(1) = 1 f(2) = 2
# f(n) = f(n-1) + f(n-2)

def rectCover(number):
    f1 = 1
    f2 = 2
    if number <= 0:return 0  #需要考虑到，全面考虑
    if number == 1:return f1
    if number == 2:return f2
    for _ in range(number-2):
        f2 , f1 = f1 + f2 , f2
    return f2

print(rectCover(3))
