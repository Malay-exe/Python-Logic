#take the two digit input and keep the 2nd digit on the power of 1st digit
def pow(n):
    x=n//10
    y=n%10
    return x**y
n=25
print(pow(n))