#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
    About BM(Boyer-Moore)
    http://zh.wikipedia.org/wiki/Boyer-Moore%E5%AD%97%E7%AC%A6%E4%B8%B2%E6%90%9C%E7%B4%A2%E7%AE%97%E6%B3%95
    About Boyer-Moore Horspool
    http://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm
"""

__version__ = "0.1"
__all__ = ["BoyerMoore"]


class BoyerMooreHorspool(object):
    def __init__(self, text, search):
        self.source = text
        self.search = search
        self.source_len = len(self.source)
        self.search_len = len(self.search)
        

    def create_skip_table(self):
        self.skip_table = {}
        for item in range(self.search_len - 1):
            self.skip_table[self.search[item]] = self.search_len - item - 1


    def match(self):
        """
            return:-1:Not found
        """
        if self.search_len > self.source_len:
            return -1
        
        self.create_skip_table()
        index = self.search_len-1
        while index < self.source_len:
            source_index = index 
            search_index = self.search_len-1
            while search_index >= 0 and self.source[source_index] == self.search[search_index]:
                source_index -= 1
                search_index -= 1

            if search_index < 0:
                return source_index+1
            
            index += self.skip_table.get(self.source[index], self.search_len)

        return -1


if __name__ == "__main__":
    #Test
    source = "tstqtttheresrkafjksdkf"
    search = "tt"
    bm = BoyerMooreHorspool(source, search)
    print bm.match()
