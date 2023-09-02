GRID_SIZE = 101

n = int(input())

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]

for k in range(n):
    a,b,c,d=map(int, input().split())
    for i in range(a,b):
        for j in range(c,d):
            grid[i][j] += 1

count = sum(1 for row in grid for cell in row if cell >= 1)

print(count)
