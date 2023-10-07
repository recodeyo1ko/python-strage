N = int(input())

rank = []

for i in range(N):
    result = input()
    count = result.count("o")
    rank.append((i, count))

sorted_rank = sorted(rank, key=lambda x: (-x[1], x[0]))

output_list = []
for r in sorted_rank:
    output_list.append(str(r[0] + 1))

output = ' '.join(output_list)

print(output)