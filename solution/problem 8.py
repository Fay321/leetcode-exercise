# -*- coding: utf-8 -*-
#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self,head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先把这个链表的值存放再list中
        lst = []
        node = head
        
        # 特殊情况
        if head==None:
            return None
        
        
        while True:
            if node.next==None:
                lst.append(node.val)
                break
            lst.append(node.val)
            node = node.next
            
        #把list转置后，再生成新的链表
        new_lst = lst[::-1]
        new_head = ListNode(new_lst[0])
        p = new_head
        for e in new_lst[1:]:
            node = ListNode(e)
            p.next = node
            p = node
        return new_head

        
        
        
        
            
if __name__=='__main__':
    # 生成链表
    lst = [1,2,3,4,5]
    
    head = ListNode(lst[0])
    p = head
    for e in lst[1:]:
        node = ListNode(e)  #节点2
        p.next = node  # 1后面是2
        p = node  