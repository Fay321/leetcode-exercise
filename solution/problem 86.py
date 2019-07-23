# -*- coding: utf-8 -*-

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #用一层一层的字典
        self.dic = dict()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        #insert这里修改了几下
        dic = self.dic
        n = len(word)-1
        for i,w in enumerate(word):
            if w in dic:
                if i!=n:
                    dic = dic[w]
                else:
                    dic[w][''] = dict()

            else:
                if i !=n:
                    dic[w] = dict() 
                    dic = dic[w]
                else:
                    dic[w] = {'':dict()}
        
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        dic = self.dic
        for w in word:
            if w not in dic:
                return False
            else:
                dic = dic[w]
        
        if '' in dic:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        dic = self.dic
        for w in prefix:
            if w not in dic:
                return False
            else:
                dic = dic[w]
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
trie.search('apple')
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")