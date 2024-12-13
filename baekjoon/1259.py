"""
백준 알고리즘 사이트 코딩테스트 연습문제 1259번 풀이코드
"""

results = []
while 1:
    sentence = list(input())

    if int("".join(sentence)) == 0:
        break

    if sentence[0] == "0":
        sentence.pop(0)

    if "".join(sentence) == "".join(sentence)[::-1]:
        results.append("yes")
    else:
        results.append("no")


for result in results:
    print(result)
