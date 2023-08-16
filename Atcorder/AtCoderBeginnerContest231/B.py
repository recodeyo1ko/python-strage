from collections import Counter

N = int(input())
S = list([input() for _ in range(N)])

S_counter = Counter(S)

max_count = S_counter.most_common()

max_count_name = max_count[0][0]

print(max_count_name)