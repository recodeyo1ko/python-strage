N, P, Q = map(int, input().split())
D = list(map(int, input().split()))

D_min = min(D)

if D_min+Q > P:
    print(P)
else:
    print(D_min+Q)