N=int(input())
for i in range(1,N+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(1,N-i+2):
        if i>=2 and i!=N:
            if j==1 or j==N-i+1:
                print(j,end=" ")
            else:
                print(end="  ")
        else:
            print(j,end=" ")
    
    print()
