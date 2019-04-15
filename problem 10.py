# -*- coding: utf-8 -*-
# kth-largest-element-in-an-array

import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        e = random.sample(nums,1)[0]
        left, mid, right = self.left_larger(nums,e)
        while True: 
            if len(left)>=k:
                e = random.sample(left,1)[0]
                left, mid, right= self.left_larger(left, e)
            elif len(left)<k and len(left)+len(mid)>=k:
                return e
            else: #len(left)<k and len(left)+len(mid)<k
                k = k -len(left)-len(mid)
                e = random.sample(right,1)[0]
                left, mid, right =self.left_larger(right, e)
                
      
    
    def left_larger(self,lst,e):
        ''' left >e ,mid==e, right <e'''
        left = []
        mid = []
        right = []
        for i in lst:
            if i>e:
                left.append(i)
            elif i==e:
                mid.append(i)
            else:
                right.append(i)
        return left,mid,right    