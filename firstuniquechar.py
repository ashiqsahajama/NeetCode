#return the index of first unique char and if it is not present return -1

#used dictionary and sorted keys based on values.First value is the first unique char. then check if value of dict and no value is equal to 1 return -1.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==1:
            return 0
        d = {}
        for i in s:
            if d.get(i)!=None:
                d[i]+=1
            else:
                d[i]=1
        res = []
        res = sorted(d,key=d.get)
        new = list(d.values())
        n = d[res[0]]
        a = 0
        for i in new:
            if i != 1:
                a+=1  
        if a == len(res):
            return -1      
        for i in range(0,len(s)):
            if s[i]==res[0]:
                return i
