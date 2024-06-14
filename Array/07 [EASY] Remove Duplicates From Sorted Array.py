##########################################################################################################################
# Leetcode 26: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# Companies: Adobe, Amazon, Apple, Google, Microsoft, Uber
# 
# Given an array sorted in ascending order, remove the duplicates while retaining their relative order.
# 
# Example 1:
#    Input: arr = [1,1,2,2,2,3,3]
#    Output: 3, [1,2,3]
# Example 2:
#    Input: arr = [1,1,1,2,2,3,3,3,3,4,4]
#    Output: 4, [1,2,3,4]
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def remove_duplicates(arr):
    n = len(arr)
    
    i = 0
    for j in range(1, n):
        if arr[j] != arr[i]:
            i += 1 
            arr[i], arr[j] = arr[j], arr[i]
    
    return (i+1), arr[:i+1]

arr = [1,1,2,2,2,3,3]
print(remove_duplicates(arr))

arr = [1,2,2,2,3,3,3,3,4,4]
print(remove_duplicates(arr))
