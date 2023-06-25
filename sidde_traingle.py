N=int(input())
for i in range(1,N+1):
    for j in range(0,i):
        print("*",end=" ")
    print()
for k in range(0,N):
    for j in range(0,N-k):
        print("*",end=" ")
    print()
        