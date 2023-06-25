# N=int(input())
# M=int(input())
# sum=0
# for i in range(N,M+1):
#     sum=sum+i

# print(sum)

# def sum(num):
#     if num==1:
#         return 1
    
#     return num+sum(num-1)
# num = int(input())
# print(sum(num))
num = 76
flag = 0
for i in range(1,num):
  if num%i==0:
    flag =flag+ 1
   	
if flag > 1:
  print('Not Prime')
else:
  print("Prime")