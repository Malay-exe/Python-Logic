#convert the string into the binary
def binary(str):
    return ' '.join(format(ord(char), '08b') for char in str)

str = "Malay"
print(f"Binary of '{str}': {binary(str)}")
