N, S, K = map(int, input().split())
price = 0

for _ in range(N):
    p, q = input().split()
    price += int(p) * int(q)

if S <= price:
    shipping_cost = 0
else:
    shipping_cost = K

print(price + shipping_cost)