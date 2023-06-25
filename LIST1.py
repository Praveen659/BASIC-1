def func(a):
    l=[]
    for i in a:
        k=i**2
        l.append(k)
    return l
N=list(map(int,input().split(",")))
print(func(N))