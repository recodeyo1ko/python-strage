n = int(input())
string_list = [input() for _ in range(n)]

success = []
for string in string_list:
    A, B = map(int, string.split(' '))
    if A + B >= 1:
        success.append(A / (A + B))

sorted_indices = sorted(range(len(success)), key=lambda i: success[i], reverse=True)

print(*(index + 1 for index in sorted_indices))

# これはエラーになる。