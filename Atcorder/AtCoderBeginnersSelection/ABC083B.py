N, A, B = map(int, input().split())

count = 0
for i in range(N+1):       
    if A <= sum(list(map(int, str(i)))) <= B:
        count += i


print(count)