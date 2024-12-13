n, k = list(map(int, input().split()))
count = 1

while True:
    if n % k == 0:
        n //= k
    else:
        n -= 1

    if n == 1:
        break
    count += 1

print(count)
