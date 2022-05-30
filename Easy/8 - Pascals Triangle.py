# Done on May 30th, 2022

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc = []                           # initialize empty list   
        i = 0                               # counter for number of rows
        
        while i < numRows:
            
            if( i == 0):                    # if it's our first row, add 1
                pasc.append([1])
                i += 1
                continue
            
            old = [0] + pasc[i-1] + [0]     # pad previous row with 0s for easier calculations
            new = []                        # initialize new empty list
            
            for j in range(len(old)-1):     # go through n-1 numbers in the last row
                num = old[j] + old[j+1]     # do a sum with the next number
                new.append(num)             # append it to the list
            pasc.append(new)                # append our new list to the pasc list
            i +=1
            
        return pasc                         # return pascal list
            

"""
118. Pascal's Triangle
Easy


Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30

"""

# Runtime: 51 ms, faster than 27.44% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 97.71% of Python3 online submissions for Pascal's Triangle.
        