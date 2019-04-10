# -*- coding: utf-8 -*-
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        J_set = set(J)
        for w in S:
            if w in J_set:
                n+= 1
        return n
