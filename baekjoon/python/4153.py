"""
백준 알고리즘 사이트 코딩테스트 연습문제 4153번 풀이코드
"""

results = []
while 1:
    nums = list(map(int, input().split()))
    if nums[0] == nums[1] == nums[2] == 0:
        break

    nums.sort()
    if nums[2] ** 2 == nums[0] ** 2 + nums[1] ** 2:
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)
