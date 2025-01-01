# User function Template for python3

class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr):
##Your code here
#Start with two variables: max_current (current maximum subarray sum ending at the current position) and max_global (maximum subarray sum found so far).
#Set both max_current and max_global to the first element of the array

#2. Traverse the Array:

#For each element starting from the second:
#Update max_current as the maximum of the current element itself or the sum of max_current and the current element.
#Update max_global if max_current exceeds max_global.
        max_current = max_global = arr[0]

        # Traverse the array from the second element
        for i in range(1, len(arr)):
            # Update the current maximum subarray sum
            max_current = max(arr[i], max_current + arr[i])

            # Update the global maximum if the current maximum is greater
            if max_current > max_global:
                max_global = max_current

        return max_global
arr= [2, 3, -8, 7, -1, 2, 3]
s=Solution()
print(s.maxSubArraySum(arr))