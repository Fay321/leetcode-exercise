# -*- coding: utf-8 -*-
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for e in s:
            if e==']':
                sub = ''
                while stack:
                    out = stack.pop()
                    if out =='[':
                        final_num = ''
                        while stack:
                            num = stack.pop()
                            if num in set('0123456789'):
                                final_num = num +final_num
                            else:
                                stack.append(num)
                                break  #得到重复次数的循环结束
                        stack.append(int(final_num)*sub)
                        break #得到有哪些字符串需要重复的结束
                    else:
                        sub  = out + sub
            else:
                stack.append(e)         
        return ''.join(stack)  

s =Solution()
print(s.decodeString("3[a2[c]]"))