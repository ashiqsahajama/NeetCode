'''
Question:
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Approch:
given input first remove all the special character and if you see a special character add a space to the new string.
Now make a dictionary will all these new string as words by array = newstring.split()

The make a list of banned words and then iterate the banned words to pop from dictionary because we cannot delete the item from dictionary by iterating.
sort and return top.
'''
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        t = ''
        for i in paragraph:
            if i.isalpha() or i.isspace():
                t += i
            else:
                t += ' '
        print(t)
        words = t.split()
        dict = {}
        for i in words:
            if dict.get(i.lower()) != None:
                dict[i.lower()]+=1
            else:
                dict[i.lower()]=1
        k = []
        for i in dict:
            if i in banned:
                k.append(i)
        for key in k:
           dict.pop(key)
        print(dict)
        res = sorted(dict,key=dict.get,reverse=True)
        return res[0]
