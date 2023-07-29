N, M = map(int, input().split())
S_list = []
for _ in range(N):
    input_string = input()
    list_S = [char for char in input_string]
    S_list.append(list_S)

answer = []

for i in range(N - 6):
    for j in range(M - 6):
        if (
            S_list[i][j] == '#' and S_list[i][j+1] == '#' and S_list[i][j+2] == '#' and S_list[i][j+3] == '.'
            and S_list[i+1][j] == '#' and S_list[i+1][j+1] == '#' and S_list[i+1][j+2] == '#' and S_list[i+1][j+3] == '.' 
            and S_list[i+2][j] == '#' and S_list[i+2][j+1] == '#' and S_list[i+2][j+2] == '#' and S_list[i+2][j+3] == '.'
            and S_list[i+3][j] == '.' and S_list[i+3][j+1] == '.' and S_list[i+3][j+2] == '.' and S_list[i+3][j+3] == '.'
            and S_list[i+5][j+5] == '.' and S_list[i+5][j+6] == '.' and S_list[i+5][j+7] == '.' and S_list[i+5][j+8] == '.'
            and S_list[i+6][j+5] == '.' and S_list[i+6][j+6] == '#' and S_list[i+6][j+7] == '#' and S_list[i+6][j+8] == '#'
            and S_list[i+7][j+5] == '.' and S_list[i+7][j+6] == '#' and S_list[i+7][j+7] == '#' and S_list[i+7][j+8] == '#'
            and S_list[i+8][j+5] == '.' and S_list[i+8][j+6] == '#' and S_list[i+8][j+7] == '#' and S_list[i+8][j+8] == '#'
        ):
          answer.append((i, j))

for i, j in answer:
    print(i+1, j+1)
