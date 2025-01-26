/*
leetcode TopInterview 150
122. Best Time to Buy and Sell Stock II
Array, Dynamic Programming, Greedy

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
 

Constraints:

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104 
 */

/**
 * @param {number[]} prices
 * @return {number}
 * 사고회로
 * 1. 금일의 주식 가격과 다음날 주식가격을 비교
 * 2. 다음날 주식 가격이 더 비싼경우, 금일 주식을 구매
 * 3. 다음날에 구매한 주식을 판매. 그리고 금일을 기준으로 다음날 가격과 비교. 마찬가지로 가격이 더 높을경우 금일 가격으로 다시 구매
 * 4. 각각의 거래에서 얻은 이익은 전부 별개이기에 모든 날을 순회하고 나서 이익들을 전부 합쳐서 return
 */
var maxProfit = function (prices) {
  let n = prices.length;
  let profit = 0;
  let buy = false;
  let hold = 0;

  for (let i = 0; i < n; i++) {
    if (buy) {
      profit += prices[i] - hold;
      buy = false;
    }

    if (i == n - 1) break;
    if (prices[i] < prices[i + 1]) {
      buy = true;
      hold = prices[i];
    }
  }

  return profit;
};
