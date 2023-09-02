N, M, P = map(int, input().split())

count = 0

for day in range(1, N+1):
    if (day - M) % P == 0:
        count += 1

print(count)