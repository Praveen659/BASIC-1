N=int(input())
for i in range(1,N+1):
    for k in range(0,N-i):
        print(end=" ")
    for j in range(1,i+1):
        if i>=3 and i!=N:
            if j==1 or j==i:
                print(j,end=" ")
            else:
                print(end="  ")
        else:
            print(j,end=" ")
    print()

