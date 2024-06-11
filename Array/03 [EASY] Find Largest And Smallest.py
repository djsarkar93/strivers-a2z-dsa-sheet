##########################################################################################################################
# Given an array arr, find the largest and the smallest elements in the array.
# 
# Example 1:
#    Input: arr = [2,5,1,3,0]
#    Output: (0, 5)
# Example 2:
#    Input: arr = [8,10,5,7,9]
#    Output: (5, 10)
##########################################################################################################################

# Optimal Solution    |    Time Complexity: O( n )    |    Space Complexity: O( 1 )
def find_mini_maxi(arr):
    n = len(arr)
    
    mini = maxi = arr[0]
    
    for i in range(1,n):
        mini = min(arr[i], mini)
        maxi = max(arr[i], maxi)
    
    return mini, maxi

arr = [2,5,1,3,0]
print(find_mini_maxi(arr))

arr = [8,10,5,7,9]
print(find_mini_maxi(arr))
