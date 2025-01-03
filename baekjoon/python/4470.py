"""
백준 알고리즘 사이트 코딩테스트 연습문제 4470번 풀이코드
"""

num = int(input())
sentences = []

for i in range(0, num):
    sentence = input()
    sentences.append(sentence)

for j in range(0, num):
    print(f"{j + 1}. {sentences[j]}")
