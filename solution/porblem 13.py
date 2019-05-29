# -*- coding: utf-8 -*-



class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        num_lst = list('1234567890')
        
        out_num_string = ''
        for w in str:
            if w==' ':
                if out_num_string =='':
                    pass
                else:
                    break
                
            elif w=='-' or w=='+':
                if out_num_string =='':
                    out_num_string += w
                else:
                    break
    
            elif w in num_lst:
                out_num_string += w
    
            else:
                break
            
 
        if self.check_not_normal_string(out_num_string):
            return 0
        else:
            new_out_num_string =''
            for e in out_num_string:
                if e=='0' and new_out_num_string in ['-','+','']:
                    pass
                elif new_out_num_string=='' and e =='+':
                    pass
                else:
                    new_out_num_string += e
        
        
        out_num_string = new_out_num_string
       
        if self.check_not_normal_string(out_num_string):
            return 0
        elif out_num_string[0]=='-':
            print(out_num_string,'aaaa')
            if self.boundary_condition(out_num_string[1:], '2147483648' ):
                return -2147483648
            else:
                return int(out_num_string)
        else:
            if self.boundary_condition(out_num_string, '2147483647' ):
                return 2147483647
            else:
                return int(out_num_string)
          
    def boundary_condition(self, out_num_string, threshold_str):
        ''' 判断不包含负号的num_string是否超过最值'''
        if len(out_num_string)>=11:
            return True
        elif len(out_num_string)==10:
            for i in range(10):
                a = out_num_string[i]
                b = threshold_str[i]
                if a<b:
                    return False
                elif a>b:
                    return True
                else:
                    pass
        else:
            return False
    
    
    def check_not_normal_string(self,out_num_string):
        '''检查这个字符串是否符合规范 '''
        if len(out_num_string.replace("-",'').replace('+',''))==0:
            return True
        elif '-' in out_num_string or '+' in out_num_string:  #处理 0+1这种情况
            for j in range(1,len(out_num_string)):
                if out_num_string[j]=='-' or out_num_string[j]=='+':
                    return True
            return False
        else:
            return False




'''
未想到的case：
1）"    +1146905820n1" 忘记把正号去掉
2）"  0000000000012345678"  首部的0要记得去掉
3）"-000000000000001" 这种情况期望输出为  -1
4） "0-1" ，"+-2" 这些情况视为错误，期望输出 0
5）"   +0 123" 用空格隔开也算隔开了，这种期望输出 0
'''