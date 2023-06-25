def is_prime(a,b):
    sum=0
    for i in range(a,b+1):
        flag=False
        for j in range(2,i):
            if i%j==0:
                flag=True
        if flag==False and i!=1 :
            sum=sum+i
    
    return sum

n=int(input())                                  
m=int(input())
print(is_prime(n,m))