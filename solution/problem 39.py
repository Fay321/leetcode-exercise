# -*- coding: utf-8 -*-
class Solution1(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out_lst = list()
        for e in candidates:
            if target>e:
                out_lst += [ [e]+lst for lst in self.combinationSum(candidates,target-e)]
            elif target==e:
                out_lst.append([e])
            else:
                pass
            
        #去掉重复
        final_out_lst = []
        for lst in out_lst:
            if sorted(lst) not in final_out_lst:
                final_out_lst.append(sorted(lst))
        return final_out_lst
    
    
class Solution(object):
    '''先将candidates排序后，然后看这个数字及之后数组能凑出target的，减少去重那项，能快很多'''
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        out_lst = list()
        candidates = sorted(candidates)  #修改
        for i in range(len(candidates)):
            e = candidates[i]
            if target>e:
                out_lst += [ [e]+lst for lst in self.combinationSum(candidates[i:],target-e)] #修改
            elif target==e:
                out_lst.append([e])
            else:
                break
            
        return out_lst

 
    
class Solution2(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """ 
        self.ans=[]
        self.combin(sorted(candidates),target,[])
        return self.ans
    
    
    def combin(self,candidated,target,subCombin):
        if target==0:
            self.ans.append(subCombin)
            return 
        for ix,num in enumerate(candidated):
            if num>target:
			### if we don't sort the candidates , this must be continue,but it is slow  
                break 
            self.combin(candidated[ix:],target-num,subCombin+[num])
        return
s =Solution()
print(s.combinationSum([8,7,4,3],11))