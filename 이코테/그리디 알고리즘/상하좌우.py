n = int(input())
movement = input().split()
x = 1
y = 1

for move in movement:
    if move == "R" and y != n:
        y += 1
    if move == "L" and y != 1:
        y -= 1
    if move == "U" and x != 1:
        x -= 1
    if move == "D" and x != n:
        x += 1

print(x, y)
