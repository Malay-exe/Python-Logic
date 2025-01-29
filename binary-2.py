#convert the string into the binary
def binary(str):
    s = ""
    for i in str:
        s += format(ord(i), '08b') + " "
    return s

str = "Malay"
print(f"Binary of '{str}': {binary(str)}")
