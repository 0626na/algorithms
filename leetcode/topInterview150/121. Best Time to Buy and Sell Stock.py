"""
leetcode Top Interview 150의 121. Best Time to Buy and Sell Stock. Array, Dynamic programming

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

from typing import List

"""
풀이과정

1. 첫번째 price 부터 하나씩 순회를 돈다.
2. 선택한 price보다 뒤에 있는 인덱스의 price에 선택한 price를 뺀다. 만약 음수면 넘어가고, 양수면 현재 최고 profit으로 가지고 있는다. 
3. prices를 하나씩 선택해서 그 선택한 price보다 뒤에 있는 price들에 선택한 price를 빼는 작업을 리스트 마지막 까지 이어간다.
4. profit을 return한다.
"""


def maxProfit(prices: List[int]) -> int:
    profit = 0
    min = prices[0]

    for stock in prices:
        if stock < min:
            min = stock
            continue
        if profit < stock - min:
            profit = stock - min

    return profit


maxProfit([2, 4, 1])
