N, M = map(int, input().split())
A_list = list(map(int, input().split()))

j = 0

for i in range(1, N + 1):
    if j < M and A_list[j] == i:
        print("0")
        j += 1
    else:
        days_until_fireworks = A_list[j] - i
        print(days_until_fireworks)
