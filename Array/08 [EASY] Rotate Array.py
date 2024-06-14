##########################################################################################################################
# Leetcode 189: Rotate Array
# Link: https://leetcode.com/problems/rotate-array/description/
# Companies: Adobe, Amazon, Apple, Google, Microsoft
# 
# Given an integer array 'arr', rotate the array left or right by k steps.
#
# Example 1:
#    Input: arr = [1,2,3,4,5,6,7], k = 3, mode = RIGHT
#    Output: [5,6,7,1,2,3,4]
# Example 2:
#    Input: arr = [-1,-100,3,99], k = 6, mode = LEFT
#    Output: [3,99,-1,-100]
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n + k )    |    Space Complexity: O( k )
def rotate_array(arr, k, mode):
    n = len(arr)
    k = k%n 
    tmp_arr = []
    
    if mode == 'LEFT':
        for i in range(0, k):
            tmp_arr.append( arr[i] )
        
        for i in range(k, n):
            arr[i-k] = arr[i]
        
        for i in range(0, k):
            arr[n-k+i] = tmp_arr[i]
            
    else:
        for i in range(n-k, n):
            tmp_arr.append( arr[i] )
        
        for i in range(n-k-1, -1, -1):
            arr[i+k] = arr[i]
        
        for i in range(0, k):
            arr[i] = tmp_arr[i]



# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1 
        end -= 1 

def rotate_array(arr, k, mode):
    n = len(arr)
    k = k%n 
    tmp_arr = []
    
    if mode == 'LEFT':
        reverse(arr, start=0, end=k-1)
        reverse(arr, start=k, end=n-1)
        reverse(arr, start=0, end=n-1)
            
    else:
        reverse(arr, start=0, end=n-k-1)
        reverse(arr, start=n-k, end=n-1)
        reverse(arr, start=0, end=n-1)



arr, k, mode = [1,2,3,4,5,6,7], 3, 'RIGHT'
rotate_array(arr, k, mode)
print(arr)

arr, k, mode = [-1,-100,3,99], 7, 'LEFT'
rotate_array(arr, k, mode)
print(arr)
