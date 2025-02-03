def rev(lst):
    y = []  
    for i in range(len(lst)-1,-1,-1):  
        y.append(lst[i]) 
    return y

lst = [1, 2, 3, 4,5,6,7]
print(rev(lst))  
