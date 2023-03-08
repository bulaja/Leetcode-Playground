# Done on Mar 8th, 2023

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        stack = [[root.left, root.right]]

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None:
                return False

            if left.val == right.val:
                stack.append([left.left, right.right])
                stack.append([left.right, right.left])

            else:
                return False
        return True
            

# Runtime 28 ms Beats 94.47% 
# Memory 14 MB Beats 52.39%

"""
101. Symmetric Tree
Easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 
Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 
Follow up: Could you solve it both recursively and iteratively?
"""