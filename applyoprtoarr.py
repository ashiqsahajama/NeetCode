#question
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed), you will apply the following on the ith element of nums:

# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0. Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.

# For example, the array [1,0,2,0,0,1] after shifting all its 0's to the end, is [1,2,1,0,0,0].
# Return the resulting array.

#firt do the operation 
#now for moving all zeros to end
#take j=0 and iterate i, if nums[i]!=0 then swap i and j and increment j because if non zero i and j will be same, if i is 0 then i is incremented and j will point to non zero and swapped,
#the swap in python is done by i,j = j,i
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]= nums[i]*2
                nums[i+1]=0
            else:
                continue
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1
        # res = []
        # j = 0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         res.append(nums[i])
        #     else:
        #         j+=1
        # for i in range(0,j):
        #     res.append(0)

        return nums

        
