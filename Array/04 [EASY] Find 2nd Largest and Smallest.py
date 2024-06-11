##########################################################################################################################
# Given an array arr, find the second largest and the second smallest elements in the array.
# 
# Example 1:
#    Input: arr = [2,5,1,3,0]
#    Output: (1, 3)
# Example 2:
#    Input: arr = [8,10,5,7,9]
#    Output: (7, 9)
##########################################################################################################################

# Brute Force Solution    |    Time Complexity: O( n log n )    |    Space Complexity: O( 1 )
def find_mini_maxi_2(arr):
    arr.sort()
    
    n = len(arr)
    #return arr[1], arr[n-2]
    
    mini, maxi = arr[0], arr[n-1]
    mini2, maxi2 = float('inf'), float('-inf')
    for i in range(0,n):
        if arr[i] != mini:
            mini2 = min(arr[i], mini2)
        
        if arr[i] != maxi:
            maxi2 = max(arr[i], maxi2)
    
    return mini2, maxi2



# Better Solution         |    Time Complexity: O( 2n )         |    Space Complexity: O( 1 )
def find_mini_maxi_2(arr):
    n = len(arr)
    
    mini = maxi = arr[0]
    for i in range(1, n):
        mini = min(arr[i], mini)
        maxi = max(arr[i], maxi)
    
    mini2, maxi2 = float('inf'), float('-inf')
    for i in range(0, n):
        if arr[i] != mini:
            mini2 = min(arr[i], mini2)
        if arr[i] != maxi:
            maxi2 = max(arr[i], maxi2)
    
    return mini2, maxi2



# Optimal Solution        |    Time Complexity: O( n )         |    Space Complexity: O( 1 )
def find_mini_maxi_2(arr):
    n = len(arr)
    
    mini, mini2 = arr[0], float('inf')
    maxi2, maxi = float('-inf'), arr[0]
    
    for i in range(1,n):
        if arr[i] < mini:
            mini2 = mini 
            mini = arr[i]
        elif arr[i] > mini and arr[i] < mini2:
            mini2 = arr[i]
        
        if arr[i] > maxi:
            maxi2 = maxi
            maxi = arr[i]
        elif arr[i] < maxi and arr[i] > maxi2:
            maxi2 = arr[i]
    
    return mini2, maxi2



arr = [2,5,1,3,0]
print(find_mini_maxi_2(arr))

arr = [8,10,5,7,9]
print(find_mini_maxi_2(arr))
