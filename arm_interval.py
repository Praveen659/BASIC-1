lower=int(input())
upper=int(input())
# n=int(input())
for n in range(lower,upper+1):


	p=len(str(n))
	sum=0
	k=n
	while(n>0):
		digit=n%10
		sum=sum+digit**p
		n=n//10
	if sum==k:
		print(k)