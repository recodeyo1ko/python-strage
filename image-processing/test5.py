from PIL import Image
import random
import matplotlib.pyplot as plt
A=[]
mat=[[0.0,0.0,0.0,0.16,0.0,0.0,0.01],
[0.85,0.04,-0.04,0.85,0.0,1.6,0.85],
[0.2,-0.26,0.23,0.22,0.0,1.6,0.07],
[-0.15,0.28,0.26,0.24,0.0,0.44,0.07]]
x=0.0
y=0.0
for k in range(0,100000):
    p=random.random()
    if p <= mat[0][6]:
        i=0
    elif p <= mat[0][6] + mat[1][6]:
        i=1
    elif p <= mat[0][6] + mat[1][6] + mat[2][6]:
        i=2
    else:
        i=3

    x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
    y  = x * mat[i][2] + y * mat[i][3] + mat[i][5]
    x = x0

    ptn=[x,y]
    A.append(ptn)

plt.figure(figsize=(10,15))
plt.scatter( *zip(*A),marker='o', color='g',s=0.1)
plt.show()