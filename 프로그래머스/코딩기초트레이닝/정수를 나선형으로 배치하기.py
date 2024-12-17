"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

양의 정수 n이 매개변수로 주어집니다. n × n 배열에 1부터 n2 까지 정수를 인덱스 [0][0]부터 시계방향 나선형으로 배치한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.
"""


def solution(n):
    answer = [[0] * n for _ in range(n)]
    count = 1
    row, col = 0, 0
    direction = "right"

    while direction != "stop":

        if direction == "check":  # 방향 확인
            if col + 1 < n and answer[row][col + 1] == 0:  # 오른쪽
                direction = "right"
                col += 1
                continue
            elif row + 1 < n and answer[row + 1][col] == 0:  # 아래
                direction = "down"
                row += 1
                continue
            elif col - 1 > -1 and answer[row][col - 1] == 0:  # 왼쪽
                direction = "left"
                col -= 1
                continue
            elif row - 1 > -1 and answer[row - 1][col] == 0:  # 위
                direction = "top"
                row -= 1
                continue
            else:
                direction = "stop"
                continue

        answer[row][col] = count
        count += 1
        ### 아래로는 이동부분 ###
        if direction == "right":  # 오른쪽
            if col + 1 == n or answer[row][col + 1] != 0:  # 더이상 갈수 없는지를 확인
                direction = "check"
                continue
            col += 1
            continue

        if direction == "down":  # 아래
            if row + 1 == n or answer[row + 1][col] != 0:
                direction = "check"
                continue
            row += 1
            continue

        if direction == "left":  # 왼쪽
            if col - 1 == -1 or answer[row][col - 1] != 0:
                direction = "check"
                continue
            col -= 1
            continue

        if direction == "top":  # 위쪽
            if row - 1 == -1 or answer[row - 1][col] != 0:
                direction = "check"
                continue
            row -= 1
            continue

    return answer


solution(5)
