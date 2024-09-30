#given array len/2 and number of pairs should be equal.
#if made a dictionary and then took the values and found the reminder by 2 and took sum for finding number of pairs
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if d.get(i)!=None:
                d[i]+=1
            else:
                d[i]=1
        a = len(nums)/2
        b = list(d.values())
        p = 0
        for i in b:
            p += i//2
        if p==a:
            return True
        else:
            return False
        
