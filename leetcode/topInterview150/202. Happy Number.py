"""
leetcode Top Interview 150 202. Happy Number. Hash Table, Math, Two Pointers

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

Example 2:

Input: n = 2
Output: false
 

Constraints:

1 <= n <= 231 - 1

"""

"""
풀이 방법
- 1이 나오지 않는 cycle이 생기는지를 확인해야 한다. 여기서 cycle이란 계속 각 자리수를 제곱해서 더할때 이전에 나왔던 숫자가 또 반복해서 나오는 경우를 말한다.
- 각 자리수 제곱의 합을 dictionary에 저장한다. 해당 값이 없으면 각 자리수의 제곱을 계속 이어가고 있다면 false를 반환한다.
- 계산을 이어가다가 각 자리 제곱의 합이 1이 나오면 True를 반환한다.
"""


def isHappy(n: int) -> bool:
    sumOfSquares = n
    hashT = {}

    while sumOfSquares != 1:
        if sumOfSquares in hashT:
            return False
        hashT[sumOfSquares] = 1
        digits = [int(s) ** 2 for s in str(sumOfSquares)]

        sumOfSquares = sum(digits)

    return True


isHappy(7)
