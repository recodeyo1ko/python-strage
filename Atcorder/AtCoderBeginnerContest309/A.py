A, B = map(int, input().split())

row_A = (A - 1) // 3
col_A = (A - 1) % 3
row_B = (B - 1) // 3
col_B = (B - 1) % 3

if row_A == row_B and abs(col_A - col_B) == 1:
    print("Yes")
else:
    print("No")