
n = map(int, input().split())
numbers = list(n)
result = []
for i in range(len(numbers)):
    result.append(numbers[i] * (2**i))

print(sum(result))