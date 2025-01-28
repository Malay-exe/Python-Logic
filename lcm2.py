#find the lcm of the given number
def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm
n,m=2,8
print(f"LCM of {n} and {m} is :",lcm(n,m)) 