# Done on: May 26th, 2022

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        minim = prices[0]
        
        for price in prices[1:]:
            
            if(price <= minim):
                minim = price
                continue
            else:
                profit = price - minim
                
                if profit > max_profit:
                    max_profit = profit
   
        return max_profit
        

# Initialize max profit as 0
# set the first day as minimum and go to the next day 
# if the price is higher than on minimum day, calculate profit and check if it is higher than max profit
# if the price is lower than on minimum day, set new minimum and continue


"""
121. Best Time to Buy and Sell Stock
Easy


You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 
Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""


# Runtime: 1005 ms, faster than 94.40% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 86.69% of Python3 online submissions for Best Time to Buy and Sell Stock.