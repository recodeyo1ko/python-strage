N, D = map(int, input().split())

list_of_D = []

for _ in range(N):
    input_string = input()
    list_N = [char for char in input_string]
    list_of_D.append(list_N)

max_continuous_leisure_days = 0

current_continuous_leisure_days = 0

for day in range(D):
    all_leisure = all(list_of_D[i][day] == 'o' for i in range(N))
    if all_leisure:
        current_continuous_leisure_days += 1
        max_continuous_leisure_days = max(max_continuous_leisure_days, current_continuous_leisure_days)
    else:
        current_continuous_leisure_days = 0

print(max_continuous_leisure_days)