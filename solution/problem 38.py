# -*- coding: utf-8 -*-


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        out_dic = dict()
        for e in strs:
            e_str = self.transform(e)
            if e_str not in out_dic:
                out_dic[e_str] = [e]
            else:
                out_dic[e_str].append(e)
        
        return list(out_dic.values())
        
            
            
        
        
    def transform(self,string):
        '''计算字母出现次数'''
        count = dict()
        for e in string:
            if e not in count:
                count[e] = 1
            else:
                count[e] += 1
        
        out_string = ''
        for key in sorted(count):
            out_string += key+str(count[key])
        return out_string
    
s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))