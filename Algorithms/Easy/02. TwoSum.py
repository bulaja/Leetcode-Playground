# Done on Feb 23rd, 2023

class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}

       for index, value in enumerate(nums):
           remaining = target - nums[index]
           
           if remaining in seen:
               return [index, seen[remaining]]
            
           seen[value] = index

# Runtime 52 ms, Beats 98.42%
# Memory 15.1 MB, Beats 39.56%


# Done on: May 25th, 2022

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0    # Counter
        
        for num in nums:
            second = target - num  # What number to look for
            
            if second in nums[index+1:]:  # Check the rest of the list
                nums.pop(index)           # Quick fix for edge case of 2 same numbers
                return [index, nums.index(second) + 1]
            
            index +=1   # Increase counter

# Runtime: 730 ms, faster than 34.41% of Python3 online submissions for Two Sum.
# Memory Usage: 15.1 MB, less than 64.13% of Python3 online submissions for Two Sum.
        

"""            
1. Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""            

