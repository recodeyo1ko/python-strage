# TLE

def is_possible(s, t):
    if s == t:
        return True
    if len(t) - len(s) == 1:
        for i in range(len(s) + 1):
            if s[:i] == t[:i] and s[i:] == t[i+1:]:
                return True
    if len(s) - len(t) == 1:
        for i in range(len(t) + 1):
            if s[:i] == t[:i] and s[i+1:] == t[i:]:
                return True
    if len(s) == len(t):
        diff_count = sum([1 for a, b in zip(s, t) if a != b])
        if diff_count == 1:
            return True

    return False

input_str = input().split()
N = int(input_str[0])
T = input_str[1]
S_list = [input() for _ in range(N)]

possible_indices = []
for i, s in enumerate(S_list, start=1):
    if is_possible(s, T):
        possible_indices.append(i)

ans_count = len(possible_indices)
if ans_count == 0:
    print("0")
else:
    print(ans_count)
    print(' '.join(map(str, possible_indices)))