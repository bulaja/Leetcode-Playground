# Done on May 31st, 2022


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        d1 = {}
        
        for char in ransomNote:
            d1[char] = d1.get(char, 0) + 1
            
        d2 = {}
        for char in magazine:
            d2[char] = d2.get(char, 0) + 1
            
        for key in d1.keys():
            if key not in d2.keys():
                return False
            
            if d1[key] > d2[key]:
                return False
        
        return True
    
            
# Go through both ransom note and magazine
# Count number of occurrences for each letter
# Go through the keys in ransom note dictionary
# and if such key does not exist in magazine dictionary, return false
# also, if value for such key is higher in ransom note than in magazine, return false
# otherwise, return True


"""
383. Ransom Note
Easy


Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""         


# Runtime: 66 ms, faster than 71.26% of Python3 online submissions for Ransom Note.
# Memory Usage: 14.1 MB, less than 53.33% of Python3 online submissions for Ransom Note.