# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

#iterate and find using string slicing from string[i to i+len(needle)] also can use string.find(needle) 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        a = len(needle)
        j = 0
        b = 0
        arr = []
        for i in range(len(haystack)):
            if haystack[i:i+a] == needle:
                return i
        return -1
        
