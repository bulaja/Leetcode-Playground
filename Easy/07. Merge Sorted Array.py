# Done on May 30th, 2022

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last = m + n - 1
      
        while m > 0 and n > 0:
            if nums1[m -1] > nums2[n - 1]:
                nums1[last] = nums1[m -1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -=1
            last -= 1
            
            
        # fill with leftover elements in nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -=1
            last - = 1
                
            
        # initiate "last" pointer
        # compare last elements of both arrays
        # write the highest one at the last pointer
        # decrement m/n depending on what array highest number came from
        # decrement last pointer
        # continue until out of elements in one array
        # if there are still elements in array nums2
        # we can just add them at the start of nums1
        # as they are already sorted
        
        
"""
88. Merge Sorted Array
Easy

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 
Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109
"""
        
# Runtime: 79 ms, faster than 6.77% of Python3 online submissions for Merge Sorted Array.
# Memory Usage: 13.9 MB, less than 38.04% of Python3 online submissions for Merge Sorted Array.
                