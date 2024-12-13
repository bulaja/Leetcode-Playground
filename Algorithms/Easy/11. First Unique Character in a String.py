Done on May 31st, 2022


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        d = {}
        for char in s:

            if char not in d.keys():
                d[char] = 1

            else:
                d[char] += 1


        if 1 in d.values():
            num_occur = list(d.values())
            dict_index = num_occur.index(next(filter(lambda i: i == 1, num_occur)))
            all_keys = list(d.keys())
            return s.find(all_keys[dict_index])

        else:
            return -1


# Go through each character in a string
# Count number of occurrences and write it in a dictionary
# if we don't have any key occurring once, return -1
# if we do, cast dictionary values to a list
# find index of the first 1 in it
# cast all key names to a list
# From keys list get what key it was based on the index
# find at what point in the string it occurred



"""
387. First Unique Character in a String
Easy

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


Example 1:

Input: s = "leetcode"
Output: 0


Example 2:

Input: s = "loveleetcode"
Output: 2


Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""

# Runtime: 133 ms, faster than 62.99% of Python3 online submissions for First Unique Character in a String.
# Memory Usage: 14.2 MB, less than 58.38% of Python3 online submissions for First Unique Character in a String.