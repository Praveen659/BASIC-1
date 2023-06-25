N=int(input())
for i in range(0,N):
    for j in range(0,i):
        print(end=" ")
    for j in range(0,N-i):
        print("*",end=" ")
    print()
for k in range(0,N):
    for j in range(0,N-k-1):
        print(end=" ")
    for j in range(0,k+1):
        print("*",end=" ")
    print()