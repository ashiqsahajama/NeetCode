'''
duplicate zero and return og len arr.

Used arr.insert(position,element)

then delete elements greater than length of orginal array.

'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        z = arr.count(0)
        l = len(arr)-1
        for i in range(l,-1,-1):
            if arr[i]==0:
                arr.insert(i,0)
        del arr[l+1:]
