# -*- coding: utf-8 -*-
"""
min stack
https://leetcode.com/problems/min-stack/
"""

class MinStack1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
       

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        if self.minValue==None:
            self.minValue = x
        else:
            self.minValue = min(self.minValue,x)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        



class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append((x, x if self.getMin() is None or x < self.getMin() else self.getMin()))
        #加入x元素后，最小值更新 （x,加入这个元素后此stack最小值）
    def pop(self):
        self.stack.pop()

    def top(self):
        return None if not self.stack else self.stack[-1][0]

    def getMin(self):
        return None if not self.stack else self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()