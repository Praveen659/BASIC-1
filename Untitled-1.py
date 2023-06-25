
# M= int(input())
# N=list(map(int,input().split()))
# count=0
# for i in range(0,M):
#     for j in range(1,M):
       
#         if N[i]>N[j]:
#             if i<j :
#                 count=count+1
# print(count)
a,b=1,10
for i in range(a,b+1):
    if i>1:

        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
