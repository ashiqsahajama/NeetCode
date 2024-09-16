# given an array we have to find the product of each element except the number.

#find product of all number before the number.Prefix Product
# find the product of all number after the number, Suffix Product
#Multiply each [i] of prefix and suffix.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1] * l
        pos = [1] * l
        res=[1]*l

        for i in range(1,l):
            pre[i]=pre[i-1]*nums[i-1]
        
        for i in range(l-2,-1,-1):
            pos[i]=pos[i+1]*nums[i+1]

        for i in range(l):
            res[i]= pre[i]*pos[i]
        return res
        


        
