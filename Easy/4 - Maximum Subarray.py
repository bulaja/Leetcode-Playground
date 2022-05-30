# Done on: May 26th, 2022

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = []
        for num in nums:
        
            if(len(max_sum) == 0):
                max_sum.append(num)
                continue

            if (num > num + max_sum[-1]):
                max_sum.append(num)
            else:
                max_sum.append(num + max_sum[-1])
        
        return max(max_sum)



# The idea is to go through each element and if it is greater than the previous contiguous array 
# largest sum + itself, start a new subarray
# otherwise, just add up the number to the sum and write the new sum down

    
"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104

"""

# Runtime: 773 ms, faster than 83.99% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 28.5 MB, less than 15.77% of Python3 online submissions for Maximum Subarray.