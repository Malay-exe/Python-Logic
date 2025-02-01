def p(s):
    return s == s[::-1]

def lp(ring):
    n = len(ring)
    x = ring   
    l = ""

    for i in range(n):
        for j in range(i + 1, i + n + 1):  
            substring = x[i:j]
            if p(substring) and len(substring) > len(l) and len(substring) <= n: 
                l = substring
    return l

s = "abacdfgdcaba"
print("Longest palindrome:", lp(s))
