N = int(input())
a = [int(i) for i in input().split()]

Alice_point  = 0
Bob_point = 0

a.sort(reverse=True)

Alice_point = sum(a[::2])
Bob_point = sum(a[1::2])

print(Alice_point - Bob_point)