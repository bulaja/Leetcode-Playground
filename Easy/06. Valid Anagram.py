# Done on Feb 26th, 2023

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Runtime 49 ms Beats 74.61%
# Memory 15.1 MB Beats 10.88%



# Done on: May 30th, 2022

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for char in s:
            if char not in d1.keys():
                d1[char] = 1
            else:
                d1[char] +=1
                
        for char in t:
            if char not in d2.keys():
                d2[char] = 1
            else:
                d2[char] +=1
            
            
        if d1 == d2:
            return True
        else:
            return False

# Runtime: 73 ms, faster than 43.27% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.5 MB, less than 66.93% of Python3 online submissions for Valid Anagram.


# Create separate dictionaries for both words
# Have unique characters act as keys in them
# Run a counter for the number of occurrences of each character
# Compare dictionaries

"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
 
Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

