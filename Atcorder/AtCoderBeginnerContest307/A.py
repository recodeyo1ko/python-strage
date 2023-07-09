N = int(input())
a = list(map(int, input().split()))
result = []
total_steps = 0

for i in range(len(a)):
    total_steps += a[i]
    if (i + 1) % 7 == 0:
        result.append(total_steps)
        total_steps = 0

print(" ".join(map(str, result)))
