def rever(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        # print(rev)
        num //= 10
    return rev
print(rever(123))