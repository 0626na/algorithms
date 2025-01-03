"""
백준 알고리즘 사이트 코딩테스트 연습문제 15829 풀이코드
"""

n = int(input())
text = list(input())

result = 0
parseAlphabetToNumber = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

for i in range(0, n):
    num = parseAlphabetToNumber[text[i]]
    squareValue = pow(31, i)
    result += num * squareValue
    result %= 1234567891

print(result)
