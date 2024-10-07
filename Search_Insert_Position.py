#Question 
#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#APProach
#So our target is to do in o(logn) so this problem is like binary search and the same procedure.


You must write an algorithm with O(log n) runtime complexity.
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while(l<=r):
            mid = (l+r)//2
            if (target<nums[mid]):
                r=mid-1
            elif (target>nums[mid]):
                l=mid+1
            else:
                return mid
        return l
        
        
        

        
