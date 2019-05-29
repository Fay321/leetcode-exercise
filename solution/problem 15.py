# -*- coding: utf-8 -*-
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        str_a = list(bin(x).split('b')[1])  #bin(4)输出为'0b100'
        str_b = list(bin(y).split('b')[1])
        
        if len(str_a)<len(str_b):
            str_a = (len(str_b)-len(str_a))*['0'] + str_a 
        else:
            str_b = (len(str_a)-len(str_b))*['0'] + str_b
        
        diff_num = 0
        for i in range(len(str_a)):
            if str_a[i]!=str_b[i]:
                diff_num += 1
        return diff_num
    
'''注意的地方就是把数字（int）转为二进制
bin(4)输出为'0b100'
'''