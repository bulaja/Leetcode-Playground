# Done on May 31st, 2022

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
    
        # Check for same number in horizontal line
        for i in range(9):
            d={}
            for j in range(9):

                item = board[i][j]

                if item == '.':
                    continue

                else:
                    if item not in d.keys():
                        d[item] = 1

                    else:
                        return False

        # Check for same number in vertical line
        for i in range(9):
            d={}
            for j in range(9):

                item = board[j][i]

                if item == '.':
                    continue

                else:
                    if item not in d.keys():
                        d[item] = 1

                    else:
                        return False     


        # Check for 3x3 grids
        for i in range(0,9,3):
            for j in range(0,9,3):
                d = {}
                test = [k[i:i+3] for k in board[j:j+3]]
                test = sum(test, [])

                for item in test:
                    if item == '.':
                        continue

                    else:
                        if item not in d.keys():
                            d[item] = 1

                        else:
                            return False 



        return True


# We have 3 separate checks
# Horizontal, vertical and 3x3 grid check
# Only if sudoku passes all 3 it will be considered valid
# Code should be written in a more concise manner,
# but since we are bound by 9x9 Sudoku's it is acceptable

"""
36. Valid Sudoku
Medium

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
 

Example 1:

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: true


Example 2:

Input: board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

Output: false

Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

"""
# Runtime: 128 ms, faster than 50.89% of Python3 online submissions for Valid Sudoku.
# Memory Usage: 14 MB, less than 34.49% of Python3 online submissions for Valid Sudoku.


