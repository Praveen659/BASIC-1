import math
N=int(input())
c=0
for i in range(0,3):
    if c>=0:
        c=N//60
        d=N/60
        new=d-c
        new=round(new*60)
print("min {0} sec {1}".format(c,new))