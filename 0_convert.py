def zero(n):
    x=str(n)
    print(n,end=' ')
    if n==0:
        print("0")
    elif n>0:
        for _ in range(n):
            x=int(x)-1
            print(x,end=' ')
    else:
        for _ in range(n,0):    
            x=int(x)+1
            print(x,end=' ')
    
n=5
zero(n)