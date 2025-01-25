"""
leetcode topInterview 150의 14. Longest Common Prefix 문제. String, Trie

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    shortest = len(min(strs, key=len))
    comparison_str = ""

    while shortest > -1:
        comparison_str = strs[0][:shortest]

        for idx, s in enumerate(strs):
            if s[:shortest] != comparison_str:
                break
            if idx == len(strs) - 1:
                return comparison_str

        shortest -= 1

    return ""


longestCommonPrefix([""])
