'''
Question
Find if word belong only to one key board row

Solution:
So iterate each word and make it as set and see if that set is a subset of the keyboard row set.
To check one set is subset of another so set(A) <= set(B)
'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first = set ()
        second = set()
        third = set()
        first = "qwertyuiop"
        second = "asdfghjkl"
        third = "zxcvbnm"
        res = []
        for i in words:
            if set(i.lower())<=set(first):
                res.append(i)
            elif set(i.lower()) <= set(second):
                res.append(i)
            elif set(i.lower()) <= set(third):
                res.append(i)


        return res
