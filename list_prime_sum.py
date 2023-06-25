def prime(list):
    sum=0
    for i in list:
        flag=False
        for j in range(2,i):
            if i%j==0:
                flag=True
        if flag==False and i!=1:
            sum=sum+i
    print(sum)
N=list(map(int,input().split()))
prime(N)