"""
leetcode Top Interview 150 20. Valid Parentheses. String, Stack

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
풀이 방법
- 열린 괄호를 스택에 push 한다.
- 닫힌 괄호가 나왔을때 stack이 있는지 확인한다. stack이 비어있으면 False
- 스택이 비어있지 않으면 맨위에 하나를 pop 한다. pop한 값과 닫힌 괄호가 틀리면 false 한다
- 문자열 순회가 끝나고 stack 값이 비어있으면 True, 남아있으면 False를 준다.
"""


def isValid(s: str) -> bool:
    stack = []
    closed = {")": "(", "}": "{", "]": "["}

    for i in s:
        if i in "([{":
            stack.append(i)
        else:
            if not stack:
                return False

            bracket = stack.pop()
            if closed[i] != bracket:
                return False

    return False if stack else True


isValid("(]")
