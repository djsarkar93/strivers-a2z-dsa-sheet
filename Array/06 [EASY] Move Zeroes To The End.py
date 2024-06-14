##########################################################################################################################
# Leetcode 283: Move Zeroes
# Link: https://leetcode.com/problems/move-zeroes/description/
# Companies: Adobe, Amazon, Apple, Google, Microsoft, Salesforce, Uber
# 
# Given an array of integers, move all the 0s to the end while keeping the order of the non-zero integers intact.
# 
# Example 1:
#    Input: arr = [1,0,2,3,0,4,0,1]
#    Output:  [1,2,3,4,1,0,0,0]
# Example 2:
#    Input: arr = [1,2,0,1,0,4,0]
#    Output:  [1,2,1,4,0,0,0]
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def move_zeroes(arr):
  n = len(arr)
  
  for i in range(0, n):
    if arr[i] == 0:
      j = i
      break
  else:
    return 
  
  for i in range(j+1, n):
    if arr[i] != 0:
      arr[j], arr[i] = arr[i], arr[j]
      j += 1
  
  return



arr = [1,0,2,3,0,4,0,1]
move_zeroes(arr)
print(arr)

arr = [1,2,0,1,0,4,0]
move_zeroes(arr)
print(arr)
