# -*- coding: utf-8 -*-
class Solution1(object):
    '''124 ms, 18M'''
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        #忘了考虑边界条件了
        if nums==[]:
            return []
        
        
        out_lst = []
        max_loc = None  #记录这个窗口中最大值所处位置，及最大值
        max_value = None
        for i in range(len(nums)-k+1):
            window_start = i
            window_end = window_start + k #左闭右开
            
            if max_value==None:
                max_value = nums[window_start]
                max_loc = window_start
                for j in range(window_start+1,window_end):
                    e = nums[j]
                    if e>=max_value:
                        max_value = e
                        max_loc = j
                out_lst.append(max_value)
            else:
                if nums[window_end-1]>=max_value:
                    max_value = nums[window_end-1]
                    max_loc = window_end-1
                elif nums[window_end-1]<max_value and window_end-max_loc<=k:
                    pass #这种情况max_value也不变
                elif nums[window_end-1]<max_value and window_end-max_loc>k:
                    #更新max_value
                    max_value= nums[window_start]
                    max_loc = window_start
                    for j in range(window_start+1, window_end):
                        e = nums[j]
                        if e>=max_value:
                            max_value = e
                            max_loc = j
                else:
                    raise
                out_lst.append(max_value)
        return out_lst
    
#============================================================#
'''尝试用双端队列来解决这道题
题目思路：https://www.jianshu.com/p/641ead99c785

使用双端队列，队列元素降序排序，队首元素为所求最大值。
滑动窗口右移，若出现的元素比队首（最大元素）大，此时清空队列，并将最大值插入队列。
若比当前值小，则插入尾部。
每次窗口右移的时候需要判断当前的最大值是否在有效范围，若不在，则需要将其从队列中删除。
'''
from collections import deque

class Solution2(object):
    '''这个尝试解答还是超时了'''
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dq = deque()  #(value, loc)
        
        #忘了考虑边界条件了
        if nums==[]:
            return []

        out_lst = []
        for i in range(len(nums)-k+1):  
            start = i 
            end = i+k  #左闭右开
            
            if start==0:
                dq.append((nums[start],start))
                for j in range(start+1,end):
                    if nums[j]>=dq[0][0]:   #如果比头部最大的都大，则清空原先dqueue
                        dq.clear()
                        dq.appendleft((nums[j],j))
                    else:  #否则，把比这个数小的筛去
                        while dq and nums[j]>=dq[-1][0]:
                            dq.pop()
                            
                        dq.append((nums[j],j))
            else:  #需要判断当前最大值是否还在范围里
                print(dq, start, end, nums[start:end])
                if dq[0][1]>=start and dq[0][1]<end:
                    pass
                else:
                    dq.popleft()
                    
                if dq and nums[end-1]>=dq[0][0]:
                    dq.clear()
                    dq.appendleft((nums[end-1],end-1))
                else:
                    while dq and nums[end-1]>=dq[-1][0]:
                        dq.pop()
                    dq.append((nums[end-1],end-1))
            
            out_lst.append(dq[0][0])
        return out_lst

#----------------------------------------------------------#
from collections import deque
 '''160ms, 18M'''
class MaxQueue:
    def __init__(self):
        self.max_q = deque()
        self.q = deque()
    
    def enqueue(self, item):
        while self.max_q and self.max_q[-1] < item:
            self.max_q.pop()

        self.q.append(item)
        self.max_q.append(item)
        
    def dequeue(self):
        popped = self.q.popleft()
        
        if popped == self.max_q[0]:
            self.max_q.popleft()
            
        return popped
        
    def get_max(self):
        if self.max_q: return self.max_q[0]
        else: return None
        

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        if not nums: return []

        q = MaxQueue()
        for num in nums[:k]:
            q.enqueue(num)
        
        results = []
        cur_max = q.get_max()
        results.append(cur_max)
        
        for i in xrange(k, len(nums)):
            cur_num = nums[i]
            q.dequeue()
            q.enqueue(cur_num)
            
            results.append(q.get_max())
        
        
        return results
s = Solution()
print(s.maxSlidingWindow([-6,-10,-7,-1,-9,9,-8,-4,10,-5,2,9,0,-7,7,4,-2,-10,8,7],7))
                








    
    
