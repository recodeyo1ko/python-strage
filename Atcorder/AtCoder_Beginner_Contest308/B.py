N, M = map(int, input().split())
Ci = input().split()
Di = input().split()
Pi = list(map(int, input().split()))

total_price = 0
for i in range(N):
    color = Ci[i]
    price = Pi[0]
    for j in range(M):
        if color == Di[j]:
            price = Pi[j+1]
            break
    total_price += price

print(total_price)
