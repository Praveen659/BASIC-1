#printing odd number of stars
N=int(input())
for i in range(1,N+1):
    for j in range(1,2*i):
        print("*",end=" ")
    print()
