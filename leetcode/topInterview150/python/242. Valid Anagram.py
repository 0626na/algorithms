"""
leetcode topInterview 150 242. Valid Anagram. Hash Table, String, Sorting

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""


def isAnagram(s: str, t: str) -> bool:
    list_s, list_t = list(s), list(t)

    list_s.sort()
    list_t.sort()

    string1 = "".join(list_s)
    string2 = "".join(list_t)

    return string1 == string2
