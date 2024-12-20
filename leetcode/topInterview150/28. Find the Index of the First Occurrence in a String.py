"""
leetcode Top Interview 150 28. Find the Index of the First Occurrence in a String. Two Pointer, String, String matching

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""

"""
풀이방법
- haystack 시작 인덱스부터 needle의 길이만큼 인덱스에 더해서 그 길이값을 비교. 일치하면 i를 인덱스에 입력. -1이거나 현재 index보다 작으면 값을 입력한다.
"""


def strStr(haystack: str, needle: str) -> int:
    needleLength = len(needle)
    index = -1

    for i in range(len(haystack)):
        if needle == haystack[i : i + needleLength]:
            if index == -1 or index > i:
                index = i

    return index
