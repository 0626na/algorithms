"""
leetcode Top Interview 150 205. Isomorphic Strings. Hash Table, String

Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Explanation:
The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

Example 2:
Input: s = "foo", t = "bar"
Output: false

Explanation:
The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

Example 3:
Input: s = "paper", t = "title"
Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""



'''
풀이방법
- 문자열 s와 문자열 t를 dictionary로 만들어서 각 문자마다 초기값 1을 준다.
- 각 문자열의 문자들을 한번씩 순회한다. 그리고 서로의 dictionary를 비교하여 1이면 해당 문자를 입력한다. 만약 문자가 입력되어있고 그 문자가 지금 순회하는 문자와 다르면 isomorphic이 아니므로 False를 반환한다
- 순회가 전부 끝나면 True를 반환
'''
def isIsomorphic(s: str, t: str) -> bool:
    dic_s={c:1 for c in s}
    dic_t={c:1 for c in t}

    # s에서 t를 매칭할때
    for i in range(len(t)):
        if dic_s[s[i]] == 1:
            dic_s[s[i]] = t[i]
        elif dic_s[s[i]] != 1 and dic_s[s[i]] != t[i]:
            return False

    
        
    # t에서 s를 매칭할때
    for i in range(len(s)):
        if dic_t[t[i]] == 1:
            dic_t[t[i]] = s[i]
        elif dic_t[t[i]] != 1 and dic_t[t[i]] != s[i]:
            return False

    return True


    

isIsomorphic('paper','title')