# Done on Mar 1st, 2023

class Solution:
    def isValid(self, s: str) -> bool:

        d = {")": "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char in d.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                if stack[-1] != d[char]:
                    return False
        
                stack.pop()
        
        if len(stack) != 0:
            return False
        
        return True
                

# Runtime 18 ms Beats 99.84% 
# Memory 13.9 MB Beats 17.80%

"""
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""