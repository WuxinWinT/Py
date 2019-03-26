# 011-二进制中1的个数

#题目描述：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

#思路：如果n!=0，n的二进制中至少有一个1

#如果1在最低位，n-1 & n 得到的数正好将这个1，变成0
#如果1不在最低位，n-1 & n 得到的数正好将这个1，变成0
#因此我们判断n-1 & n能够循环运行的次数就可以判断二进制中有多少个1了。

# 在python中需要使用c_int()函数不然负数不会变成0.



def NumberOf1(n):
        # write code here
    count = 0
    if n < 0:
        n = n & 0xffffffff #相当于变成不带符号的数了
    while n:
        count += 1
        n = (n - 1) & n
    return count

print(NumberOf1(-7)) # ffffff 1111 1001 (30个)
