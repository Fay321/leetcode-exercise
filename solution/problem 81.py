# -*- coding: utf-8 -*-
'''自己尝试写的解答，虽然通过了，但是太耗时'''
class LRUCache1(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.used_time  = dict()  #记录某个key被get、put的时间戳。返回时间戳对应最小的那个key
        self.time_stamp = 0
        self.dic = dict()
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        self.time_stamp += 1
        
        if key in self.dic:
            self.used_time[key] = self.time_stamp
            return self.dic[key]
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.time_stamp += 1
        if key in self.dic:
            self.dic[key]=value
            self.used_time[key] = self.time_stamp
        else:
            if len(self.dic)==self.capacity:
                least_used_key = sorted(self.used_time.items(),key=lambda s:s[1])[0][0]
                self.dic.pop(least_used_key)
                self.used_time.pop(least_used_key)
                
            self.dic[key]=value
            self.used_time[key] = self.time_stamp
        

'''
OrderedDict is a subclass of a dict with features of the Double Linked List. It stores original dict as well as mapping of keys to links in a doubly linked list
from : discussion board
'''
from collections import OrderedDict

class LRUCache2:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.dict.move_to_end(key)
        return self.dict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.dict.pop(key)
            
        self.dict[key] = value
        if len(self.dict) > self.cap:
            self.dict.popitem(last=False) 

'''
不借助OrderedDict，用dict+双向链表实现
from: https://leetcode.com/problems/lru-cache/discuss/274033/Python-136ms-linked-list-O(1)-no-imports-debug-attached
'''
class DLinkedList:
    def __init__(self):
        self.key  = 0
        self.val  = 0
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        
        self.head = DLinkedList()
        self.tail = DLinkedList()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        '''
        If the requested cache not exist return -1, otherwise, return it is value and
            move it to the top of the cache (to mark it as a latest visited so it will not be removed)
        '''
        if key not in self.cache:
            return -1
        requestedNode = self.cache[key]
        self.moveNodeToTop(requestedNode)
        
        return requestedNode.val

    def put(self, key,value):
        '''
        Add new node to the top of the head and if the cache capacity reached we just need to remove
            the least recently used cache and it will be at the end of course so remove it and add
            the new item to the top of the cache.
        But what if the node already there so just move it to the top, and you done.
        '''
        node = self.cache.get(key, None)
        if not node:
            newNode = DLinkedList()
            newNode.key = key
            newNode.val = value
            
            self.addNodeToTop(newNode)
            # store it in our cache
            self.cache[key] = newNode
            self.size += 1
            
            # if our cache size exceeds our capacity remove the least used cache
            if self.size > self.capacity:
                removedNode = self.removeLeastUsedNode()
                del self.cache[removedNode.key]
                self.size -= 1
        else:
            node.val = value
            self.moveNodeToTop(node)
    
    def addNodeToTop(self, node):
        '''
        Adding new node in the fron of the cache, latest accessed by client
        '''
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
    
    def removeNode(self, node):
        '''
        Remove node from the list from any place
        '''
        prevNode = node.prev
        nextNode = node.next
        
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def moveNodeToTop(self, node):
        '''
        Move the latest accessed node to be in the beginning of the cache
        '''
        self.removeNode(node)
        self.addNodeToTop(node)
    
    def removeLeastUsedNode(self):
        '''
        Use this function to remove the least recently used node
        '''
        node = self.tail.prev
        self.removeNode(node)
        return node
 
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
