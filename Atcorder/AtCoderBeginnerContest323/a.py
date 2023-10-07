S = input()

frag = 0

for i in range(2, 17, 2):
    if S[i - 1] == '0':
        frag = 1
    else:
        frag = 0
        break
        
if  frag == 1:
    print("Yes")
else:
    print("No")