
def find(target,array):
    i = 0
    j = len(array[0]) - 1  #len(array[0]) 为列数
    while i < len(array) and j >= 0: #len(array) 为行数
        base = array[i][j]
        if target == base:
            return True
        elif target > base:
            i += 1
        else:
            j -= 1
    return False

print(find(4,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))


# 出现错误:列数行数，且此题中二维数组不一定是正方形

