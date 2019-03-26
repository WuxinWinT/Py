# 013-调整数组顺序使奇数位于偶数前面

#思路:遍历一次，统计奇数个数。然后从前往后填坑

def reOrderArray(array):
    odd_cnt = 0
    res = [0] * len(array)

    for n in array:
        if n % 2 != 0:   # 统计奇数个数
            odd_cnt += 1
    # 填坑
    odd_i = 0
    even_i = odd_cnt #不用减1
    for i in range(len(array)):
        if array[i] % 2 != 0:
            res[odd_i] = array[i]
            odd_i += 1
        else:
            res[even_i] = array[i]
            even_i += 1
    return res
    

    
