"""
백준 알고리즘 사이트 코딩테스트 연습문제 16433번 풀이코드
"""

nums = list(map(int, input().split()))
n = nums[0]
r = nums[1]  # 행
c = nums[2]  # 열

for row in range(1, n + 1):
    farm = []
    for col in range(1, n + 1):
        # 초기 좌표의 행과 열의 짝수 홀수가 일치할때
        if r % 2 == row % 2:
            if c % 2 == col % 2:
                farm.append("v")
            else:
                farm.append(".")

        # 초기 좌표의 행과 열의 짝수 홀수랑 반대일때
        if r % 2 != row % 2:
            if c % 2 != col % 2:
                farm.append("v")
            else:
                farm.append(".")

    print("".join(farm))
