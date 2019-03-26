
def replaceSpace(s):
    s_len = len(s)
    space_count = 0
    for i in s:
        if i == ' ':
            space_count += 1
    s_len += 2 * space_count    # ' ' 替换成 '%20',多了2个字符
    new_array = [' '] * s_len  # eg:[' ', ' ', ' ', ' ', ' ']
    j = 0
    for i in range(len(s)):   #  range() 函数可创建一个整数列表，一般用在 for 中
        if s[i] == ' ':
            new_array[j] = '%'
            new_array[j+1] = '2'
            new_array[j+2] = '0'
            j += 3
        else:
            new_array[j] = s[i]
            j += 1
    return ''.join(new_array)
# join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串
# str = "-";
# seq = ("a", "b", "c"); # 字符串序列
# print str.join( seq );
# OUT: a-b-c

print(replaceSpace('We Are Happy'))


#为错误的地方

#    def replaceSpace(self, s):
#        s_len = len(s)
#        space_count = 0
#        for i in s:  
#            if i == ' ':  #i,不是s(i)
#                space_count += 1
#        s_len += space_count * 2
#        new_array = [' '] * s_len
#        j = 0
#        for i in range(len(s)):
#            if s[i] == ' ':      #s[i],不是s(i)
#                new_array[j] = '%'
#                new_array[j+1] = '2'
#                new_array[j+2] = '0'
#                j += 3
#            else:
#                new_array[j] = s[i]
#                j += 1
#        return ''.join(new_array)


#也可以看出： for i in s 与 for i in range(len(s)) 的区别
