N=int(input())
FLAG=0
for i in range(1,N+1):
    if(N%i)==0:
        FLAG=FLAG+1
if(FLAG==2):
    print("prime")
else:
    print("not prime")