# Done on Feb 24th, 2023

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        if r*c != m * n:
            return mat

        flattened = sum(mat, [])

        new_mat = r *[c * [0]]

        for i in range(0,r):
            new_mat[i] = flattened[c*i:c*(i+1)]
                
        return new_mat

# Runtime 84 ms, Beats 94.29%
# Memory 14.7 MB, Beats 28.70%


# Done on May 30th, 2022

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        if ((r * c) != (len(mat) * len(mat[0]))):   # if not possible, return original matrix
            return mat
            
        new_mat = []                                # initialize empty list
        row_num = 0                                 # set counters for row and columns
        col_num = 0

        for i in range(r):                          # for loop over number of rows of the new matrix
            temp = []
            for j in range(c):                      # for loop over number of columns of the new matrix
                temp.append(mat[row_num][col_num])  # add elements to the list
                col_num +=1

                if (col_num == (len(mat[0]))):      # if we get to the end of the original matrix
                    row_num +=1                     # go to the next row
                    col_num = 0                     # and reset column count
            



            new_mat.append(temp)                    # add a row to the list

        return new_mat


# Runtime: 129 ms, faster than 43.65% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 14.8 MB, less than 13.82% of Python3 online submissions for Reshape the Matrix.


"""
566. Reshape the Matrix
Easy


In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 
Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

"""   