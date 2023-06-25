def is_prime(num):
    sum=0
    
    flag=false
    for j in range(2,num):
        if num%j==0:
            flag=true
            break
    

        sum=sum+num
    
    return sum

n=int(input())
m=int(input())
for i in range(n,m+1):
    is_prime(i)