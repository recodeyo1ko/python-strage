K, G, M = map(int, input().split())

glass = 0
mag_cup = 0

for _ in range(K):
    if glass >= G:
        glass = 0
    elif mag_cup == 0:
        mag_cup = M
    else:
        transfer = min(G - glass, mag_cup)
        glass += transfer
        mag_cup -= transfer

print(glass, mag_cup)