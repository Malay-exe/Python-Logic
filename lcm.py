#find the lcm of the given number
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
n = 2
m = 3
res = lcm(n, m)
print(f"LCM of {n} and {m} is: {res}")