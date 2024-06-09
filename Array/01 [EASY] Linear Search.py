##########################################################################################################################
# Linear Search: Given an array 'arr' and a number 'num', if 'num' is in 'arr', return 'num's index; otherwise, return -1.
# 
# Example 1:
#    Input: arr = [1,2,3,4,5], num = 
#    Output: 2
# Example 2:
#    Input: arr = [5,4,3,2,1], num = 15
#    Output: -1
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def linear_search(arr, num):
  n = len(arr)
  
  for i in range(0, n):
    if arr[i] == num:
      return i
  
  return -1

arr, num = [1,2,3,4,5], 3
print(linear_search(arr, num))

arr, num = [5,4,3,2,1], 15
print(linear_search(arr, num))
