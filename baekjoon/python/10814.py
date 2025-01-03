"""
백준 알고리즘 사이트 코딩테스트 연습문제 10814번 풀이코드
"""

# 입력받을 회원수
n = int(input())
members = []

# 회원의 나이와 이름을 입력
for i in range(n):
    applicant = list(input().split())
    members.append({"age": int(applicant[0]), "name": applicant[1], "order": i})

# 파이썬의 람다함수를 활용하여 회원리스트를 정렬,
# 나이로 먼저 내림차순으로 정렬하고 나이가 같을경우 가입순서 (여기서는 입력순서)로 정렬한다.
# 튜플을 이용해서 정렬 기준을 부여한다.
members.sort(key=lambda member: (member["age"], member["order"]))

# 나이와 이름을 출력
for member in members:
    print(f'{member["age"]} {member["name"]}')
