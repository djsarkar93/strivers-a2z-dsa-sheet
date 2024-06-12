##########################################################################################################################
# Leetcode 485: Max Consecutive 1s
# Link: https://leetcode.com/problems/max-consecutive-ones/description/
# Companies: Amazon, Adobe, Google, Microsoft
# 
# Given an array containing only 1s and 0s, return the count of the maximum number of consecutive 1s in the array.
# 
# Example 1:
#    Input: arr = [1,1,0,1,1,1]
#    Output: 3
# Example 2:
#    Input: arr = [1,0,1,1,0,1] 
#    Output: 2
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def find_max_consecutive_ones(arr):
    n = len(arr)
    counter = max_counter = 0
    
    for i in range(0, n):
        if arr[i] == 1:
            counter += 1 
        else:
            counter = 0
        
        max_counter = max(counter, max_counter)
    
    return max_counter



arr = [1,1,0,1,1,1]
print(find_max_consecutive_ones(arr))

arr = [1,0,1,1,0,1]
print(find_max_consecutive_ones(arr))
