# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

#so we can iterate a dictionary by items ans two iterators.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d ={}
        for i in nums:
            if d.get(i)!=None:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                return i
        
