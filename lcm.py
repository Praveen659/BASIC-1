def lcm(x,y):
    if x<y:
        higher=y
    else:
        higher=x
    siv=higher
    while(True):
        if (higher%x==0) and (higher%y==0):
            return higher
    
        higher=higher+siv
        

a=int(input())
b=int(input())
print(lcm(a,b))