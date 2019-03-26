# 012-数值的整数次方

#题目描述：给定一个double类型的浮点数base和int类型的整数exponent。
# 求base的exponent次方。

#思路：指数幂的所有边界包括:
#指数为0的情况，不管底数是多少都应该是1
#指数为负数的情况，求出的应该是其倒数幂的倒数
#指数为负数的情况下，底数不能为0

def Power(base, exponent):
    if exponent == 0: return 1
    flag = 1
    if exponent < 0:
        exponent *= -1 #变正
        flag = 0
    temp = base
    res = 1
    while(exponent):
        if exponent & 1:    # 1其实是0000 0001
            res *= temp     #eg: 3^5 (5=4+0+1:101)（2^2  + 2^0） 
        temp *= temp        #res=3，3*3，res=3* 3*3 * 3*3 
        exponent = exponent >> 1   #二进制右移

    return res if flag else 1.0/res

print(Power(2, -2))

