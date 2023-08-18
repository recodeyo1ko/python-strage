N,Q=map(int,input().split())
A=[(a,10**9) for a in map(int,input().split())]
X=[]
for i in range(Q):
  x=int(input())
  X.append((x,i))

AX=sorted(A+X)[::-1]

ans=[0]*Q
cnt=0
for x,i in AX:
  if i<Q:
    ans[i]=cnt
  else:
    cnt+=1

print(*ans,sep="\n")