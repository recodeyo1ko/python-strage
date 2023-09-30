N, M = map(int, input().split())
S = input()
T = input()

for i in range(len(S)):
    if S == T[0:len(S)] and S == T[len(T) - len(S):len(T)]:
        print("0")
        break
    elif S == T[0:len(S)]:
        print("1")
        break
    elif S == T[len(T) - len(S):len(T)]:
        print("2")
        break
    else:
        print("3")
        break

