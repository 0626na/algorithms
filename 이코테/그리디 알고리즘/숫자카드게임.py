n, m = map(int, input().split())
minValue = 0


for i in range(n):
    temp = list(map(int, input().split()))
    minValue = min(temp)

print(minValue)
