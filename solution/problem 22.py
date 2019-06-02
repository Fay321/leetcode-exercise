# -*- coding: utf-8 -*-
class Solution1(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        if len(T)<=1:
            return [0]
        
        
        final_out = dict()  #index:value  #记录的从右往左的值

        for j in range(len(T)-1,-1,-1):
            a = T[j]
            
            if j==len(T)-1:
                final_out[j] = 0
            else:
                i = j+1
                while True:
                    if i>=len(T):
                        break
                    else:
                        b = T[i]
                        if b<=a:
                            if final_out[i]==0:
                                break
                            else:
                                i += final_out[i]
                        else:
                            final_out[j] = i-j
                            break
                           
                
                if j not in final_out:
                    final_out[j] = 0
        
        final_out_lst = []
        for k in range(len(T)):
            final_out_lst.append(final_out[k])
        return final_out_lst
    

class Solution2(object):
    '''这个解法速度更快。'''
    def dailyTemperatures(self, T):
        res = [0 for i in range(len(T))]
        stack = []
        for i in range(len(T)):
            while stack and T[i] > T[stack[-1]]: 
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res      
        
        
        
    
s = Solution2()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
                    
        