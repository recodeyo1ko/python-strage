N = int(input())
d = [int(input()) for i in range(N)]

d.sort(reverse=True)
d = list(set(d))
print(len(d))