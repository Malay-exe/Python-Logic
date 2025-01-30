#check whether the first and the last numbers are same in the list
def check(lst):
    return True if lst[0]==lst[-1] else False
lst=[1,2,3,4,5,1]
print(check(lst))
