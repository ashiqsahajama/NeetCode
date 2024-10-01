#given one input array, divide content into array then for every element check the last element and place in largest item
class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []
        arr1.append(nums[0])
        arr2.append(nums[1])

        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        arr3 = arr1 + arr2
        return arr3
