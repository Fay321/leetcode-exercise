# -*- coding: utf-8 -*-

from numpy import median
class Solution1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        lst = nums1+nums2
        return median(lst)
    
    
class Solution(object):
    '''转化为求第k小的数'''
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if (m+n) %2 ==1:
            k = (m+n)//2 +1
            return self.find_smallest_k(nums1,nums2, k)
        else:
            k = (m+n)//2
            return 0.5*(self.find_smallest_k(nums1,nums2,k)+self.find_smallest_k(nums1,nums2,k+1))
    def find_smallest_k(self, nums1, nums2, k):
        if nums1==[] and nums2!=[]:
            return nums2[k-1]
        elif nums1!=[] and nums2==[]:
            return nums1[k-1]
        elif nums1==[] and nums2==[]:
            if k!=0: raise
        else:
            if k==1:
                return min(nums1[0], nums2[0])
        
        m = min(k//2, len(nums1))
        n = min(k//2, len(nums2))
        a = nums1[m-1]
        b = nums2[n-1]
        if a<b:
            return self.find_smallest_k(nums1[m:],nums2,k-m)
        else:
            return self.find_smallest_k(nums1,nums2[n:],k-n)