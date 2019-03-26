# 019-顺时针打印矩阵

class Solution:
    def printMatrix(self,matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = [[each[i] for each in matrix] for i in range(len(matrix[0]))][::-1] if matrix else []  
        return res
#注释：

[[each[i] for each in matrix] for i in range(len(matrix[0]))][::-1]:矩阵转置
[::-1]逆序输出
[1 2]
[3 4]

[1 3]
[2 4]

:逆序
[2 4]
[1 3]

