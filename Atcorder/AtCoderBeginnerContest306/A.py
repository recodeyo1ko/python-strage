N = int(input())
S = input()
new_list = []
for c in S:
    new_list.append(c*2)
out = ''.join(new_list)

print(out)