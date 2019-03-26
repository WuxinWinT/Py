# 006-旋转数组的最小数字

# 描述：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

#思路：总体二分：
#if mid大于left, left = mid
#if mid小于left, right = mid
#直到mid<mid-1位置的数

def minNumberInRotateArray(rotateArray):
    # write code here
    if not rotateArray:
        return 0
    low = 0
    high = len(rotateArray) - 1
    while True: 
        mid = (low + high) // 2
        #取整除 - 返回商的整数部分（向下取整:只要后面有小数忽略小数） 5//2=2
        if rotateArray[mid] >= rotateArray[low]:
            low = mid
        else:
            high = mid
        if rotateArray[mid] < rotateArray[mid - 1]: #非减排序， mid-1 < mid
            return rotateArray[mid]

print(minNumberInRotateArray([3,4,5,1,2]))
print(minNumberInRotateArray([1,1,1,0,1]))
print(minNumberInRotateArray([]))

# 核心：非减排序的数组的一个旋转
# eg：1234567  4567123   6712345
