"""
백준 알고리즘 사이트 코딩테스트 연습문제 30802번 풀이코드
"""

# 참가자 수
n = int(input())

# 각 사이즈별 티셔츠 수
tShirts = list(map(int, input().split()))
s = tShirts[0]
m = tShirts[1]
l = tShirts[2]
xl = tShirts[3]
xxl = tShirts[4]
xxxl = tShirts[5]

# 티셔츠 묶음수와 펜 묶음수
bundles = list(map(int, input().split()))

# 티셔츠 묶음
tshirtsBundle = bundles[0]
# 펜 묶음
penBundle = bundles[1]

# 필요한 최소 티셔츠 묶음 수
minimunTshirtsBundle = 0

# 티셔츠 묶음 최소 몇개 필요한지 계산
for tshirt in tShirts:
    if tshirt == 0:
        continue
    minimunTshirtsBundle += tshirt // tshirtsBundle
    if tshirt % tshirtsBundle != 0:
        minimunTshirtsBundle += 1


print(minimunTshirtsBundle)
print(f"{n//penBundle} {n%penBundle}")
