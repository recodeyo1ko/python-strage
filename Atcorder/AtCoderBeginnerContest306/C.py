n = int(input())
a = list(map(int, input().split()))
cnt = [0 for _ in range(3 * n)]
ans = []
for i in a:
    cnt[i] += 1
    if cnt[i] == 2:
        ans.append(i)

## listだったらスペース区切りで出力
print(*ans)
