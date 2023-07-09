N, K = map(int, input().split())
prescriptions = []

# 薬の情報を読み取る
for _ in range(N):
    a, b = map(int, input().split())
    prescriptions.append((a, b))

day = 1  # 初めの日数

# K錠以下になる日を探す
while True:
    total_pills = sum(b for _, b in prescriptions)  # その日の薬の総錠数
    for i in range(N):
        a, b = prescriptions[i]
        total_pills -= (day - 1) // a * b

    if total_pills <= K:
        break

    day += 1

print(day)