N = int(input())
C_list = []
A_list_all = []

for _ in range(N):
    C_i = int(input())
    A_i = list(map(int, input().split()))
    C_list.append(C_i)
    A_list_all.append(A_i)

X = int(input())

indices = [index + 1 for index, A_list in enumerate(A_list_all) if X in A_list]
C_list_inclide_X_depends_A_list = [C_list[i - 1] for i in indices if C_list[i - 1] != 0]

if len(C_list_inclide_X_depends_A_list) > 0:
    C_list_inclide_X_depends_A_list_min = min(C_list_inclide_X_depends_A_list)
    C_list_inclide_X_depends_A_list_count = C_list_inclide_X_depends_A_list.count(C_list_inclide_X_depends_A_list_min)

    print(C_list_inclide_X_depends_A_list_count)
    indices_filtered = [index for index in indices if C_list[index - 1] == C_list_inclide_X_depends_A_list_min]
    print(" ".join(map(str, indices_filtered)))
else:
    print("0\n")
