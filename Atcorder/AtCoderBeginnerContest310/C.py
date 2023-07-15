N = int(input())
S_list = [input() for i in range(N)]

def is_same_bar(s1, s2):
    return s1 == s2 or s1 == s2[::-1]

bar_set = set()

for i in range(N):
    unique = True
    for j in range(i + 1, N):
        if is_same_bar(S_list[i], S_list[j]):
            unique = False
            break
    if unique:
        bar_set.add(S_list[i])

num_unique_bars = len(bar_set)
print(num_unique_bars)
