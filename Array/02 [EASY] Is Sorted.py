##########################################################################################################################
# Given an array arr, return True if the array is sorted in ascending order; otherwise, return False.
# 
# Example 1:
#    Input: arr = [1,2,3,4,5]
#    Output: True
# Example 2:
#    Input: arr = [5,4,6,7,8]
#    Output: False
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def is_sorted(arr):
  n = len(arr)
  
  for i in range(1, n):
    if arr[i-1] > arr[i]:
      return False
  
  return True

arr = [1,2,3,4,5]
print(is_sorted(arr))

arr = [5,4,6,7,8]
print(is_sorted(arr))

##########################################################################################################################
# Leetcode 1752: Check if rotated array was originally sorted
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
# Companies: Adobe, Amazon
# 
# Example 1:
#    Input: arr = [3,4,5,1,2]
#    Output: True    {Explanation: [1,2,3,4,5] is the original sorted array.}
# Example 2:
#    Input: arr = [2,1,3,4]
#    Output: False    {Explanation: There is no sorted array which once rotated that can make arr}
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def was_originally_sorted(arr):
  n = len(arr)
  counter = 0
  
  for i in range(0, n):
    i_next = 0 if i == n-1 else i+1
    
    if arr[i] > arr[i_next]:
      counter += 1
      if counter > 1:
        return False
  
  return True

arr = [3,4,5,1,2]
print(was_originally_sorted(arr))

arr = [2,1,3,4]
print(was_originally_sorted(arr))

arr = [1,2,3]
print(was_originally_sorted(arr))
