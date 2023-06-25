N=int(input())
c=0
for i in range(0,2):
    if c>=0:
        c=N//60
        d=N/60
        new=d-c
        new=round(new*60)
print("min {0} sec {1}".format(c,new))

    # if c>24:
    # d=c/60
    # print(d)
    # if d>24:
    #     e=d-24
    #     print(e)
