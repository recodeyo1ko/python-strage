N = int(input("要素数を入力してください: "))
s_list = []

for i in range(N):
    s = input(f"s{i+1}を入力してください: ")
    s_list.append(s)

print(s_list)
