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

- 리스트 맨 첫번째 주식가격을 최소 가격으로 설정
- 순회하면서 현재 최소가격보다 낮으면 그 값을 최소가격으로 바꾸고 다음 값으로 continue
- 현재 최소가격보다 높으면 뺄셈. 현재 이익보다 크면 변경
- 순회가 끝나고 profit을 return
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
