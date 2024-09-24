#give a string treee the result should be eeetr becauase frequency of e is 3, rest are one each.

#for this make a char frequency dictionary. Then use sorted function and sort dictionary based on its value and get keys.
#the sorting can be done using sorted function that takes 3 arguments. the data to sort,key to get, reverse. sorted(d,key = d.get,reverse =True)
#where key = d.get is a method that retrieves the value associated with a key in the dictionary.
#then print by taking new string and multiply value with key.
class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        res = ""
        for i in s:
            if d.get(i)!=None:
                d[i]+=1
            else:
                d[i]=1
        sortd = []
        sortd = sorted(d,key=d.get,reverse=True)
        for i in sortd:
            res += i*d[i]
        return res
