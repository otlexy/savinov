from math import * 
print('Введите Xbeg, Xend, Dx и Eps') 
xb = float(input('Xbeg=')) 
xe = float(input('Xend=')) 
dx = float(input('Dx=')) 
eps = float(input('Eps=')) 
print("+--------+--------+-----+") 
print("I   X    I    Y   I  N  I") 
print("+--------+--------+-----+") 
xt = xb 


while xt <= xe: 
    an = 1/xt
    n = 0
    y = an 
    while True:
        n+=1
        an=((-1)**n)/((xt**(2*n+1))*(2*n+1))
        y+=an 
        if abs(an) < eps: 
            break
    y=pi/2-y
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(xt,y,n)) 
    xt = xt + dx 
print("+--------+--------+-----+")
