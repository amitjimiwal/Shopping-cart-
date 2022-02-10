def a2s(s):
    x=''
    l = len(s)
    n = 0
    for i in range(l):
        n=n*10 + int(s[i])
        if (n >= 32 and n <= 126):
         c = chr(n)
         x += str(c)
         n=0
    return x
def s2a(s):
    x=''
    for i in s:
        x+= str(ord(i))
    return x