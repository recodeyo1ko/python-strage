N, M = map(int, input().split())
PCF_list = [list(map(int, input().split())) for i in range(N)]

P_list = [row[0] for row in PCF_list]
C_list = [row[1] for row in PCF_list]
F_list = [row[2:] for row in PCF_list]

def has_superior_product(i, j):
    if P_list[i] < P_list[j]:
        return False
    
    for f in F_list[i]:
        if f not in F_list[j]:
            return False
    
    if P_list[i] > P_list[j] or len(F_list[j]) > len(F_list[i]):
        return True
    
    return False

result = "No"

for i in range(N):
    for j in range(N):
        if i != j and has_superior_product(i, j):
            result = "Yes"
            break

print(result)
