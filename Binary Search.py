'''
Implement to find the target number in array and find in log n time complexity.

So this can be done using while loop and have a low and high at first and last index.
see where is the target , if it is less than mid change high to mid -1 and compute mid
if it is more than mid change low to mid+1 and compute mid return mid if not.
But if loop ended return -1 saying nothing is found
'''

def solution(arr,x):
  l = 0
  h = len(arr)-1

  while(l<=h):
    m = (l+h)//2

  if (arr[m]<x):
    h = m-1
  elif(arr[m]>x):
    l = m+1
  else:
    return mid 
return -1
