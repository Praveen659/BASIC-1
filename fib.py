N=int(input())
n1=0
n2=1
# while(N>0):
#     print(n1)
#     s=n1+n2
#     n1=n2
#     n2=s
#     N=N-1
count=0
while(count<N):
    print(n1)
    s=n1+n2
    n1=n2
    n2=s
    count+=1            
