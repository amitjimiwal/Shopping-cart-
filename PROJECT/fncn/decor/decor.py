#2d Tuple Decorator
def max(t,k):
    z = 1
    for i in t:
        x = i[k]
        if z < len(str(x)):
            z = len(str(x))
        else:
            continue
    else:
        return z  
def noc(t):
    count=0
    for i in t[0]:
        count+=1
    return count
def row(t):
    count = 0
    for i in t:
        count += 1
    return count    
def decor(t):
    x=''
    for i in range(noc(t)):
        x+= '+'+'-'*(max(t,i))
    else:
        x+='+'
        print(x,end='\n')
    y=''
    for j in range(row(t)):
        for i in range(noc(t)):
            y+='|' + f'{str(t[j][i])}' + ' '*(max(t,i) - len(str(t[j][i])))
        else:
            y+='|'
            print(y,end='\n')
            y=''
    else:
        print(x,end='\n')

def ats(z):
    x=''
    for i in z:
        x += str(i) + ' '
    x = x.rstrip(' ')
    return x